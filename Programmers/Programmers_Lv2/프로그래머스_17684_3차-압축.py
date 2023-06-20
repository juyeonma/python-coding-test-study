'''
# 프로그래머스_17684_[3차] 압축. Lv 2. 풀이: 23.06.08

# How to
## 1. 
- w와 c의 인덱스를 조정해가면서, 딕셔너리에 존재하는지 탐색한다.
- w: 0부터 시작, c: 반복문에서 맨 끝 인덱스부터 거꾸로.
    - 딕셔너리에 존재하는 문자열을 찾으면, c가 새로운 w가 된다.

## 2. for문 탐색 범위를 앞에서부터: 속도가 엄청 빨라짐
- 1번 방법과 같은데, 범위만 변경하고 dic에 없는 key인지를 판별했다.
    - dic에 없다면, 직전 index까지는 dic에 존재한다는 뜻
- 입력 문자열에 공백을 더해서, while이 무한루프에 빠지지 않도록 했다.
    - 맨 마지막에 dic에 없는 문자열이 있어야만 if문에 걸려서 while이 종료 가능하다.
- 

# Review
- for문에서 범위 때문에 조금 헤맸는데, 과정 자체가 어렵지는 않았다.
- 예전에 비슷한 문제를 풀었던거 같기도 하고..
- 다만 다른 사람 풀이에 비해서 시간이 매우매우 많이..걸렸다..
    - chr을 배웠다. 
- 스터디원의 풀이를 보고, 2번 코드를 작성했다.
    - index의 탐색범위를 앞에서부터 하고 dic에 없는지를 판별했다.
    - 특히 입력 문자열 뒤에 공백을 더해 while문이 종료되게 한 것이 너무 신선했다.
    - 시간이 엄청 단축됐다.. 1번 코드는 뒤에서부터 탐색해서 속도가 느렸나 보다.
'''

# 1. 성공 Code
def solution(msg):
    answer = []
    dic = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))
    w = 0
    cnt = 26
    n = len(msg)
    # 문자열을 넘어서지 않는 범위 내에서 탐색
    while w < n:
        # 맨 뒤에서부터 탐색
        for c in range(n, w, -1):
            if msg[w:c] in dic:
                answer.append(dic[msg[w:c]])
                cnt += 1
                # 사전에 추가
                dic[msg[w:c+1]] = cnt
                # w 갱신
                w = c
                break
    return answer


# 2. for문 탐색 범위를 앞에서부터: 속도가 엄청 빨라짐
def solution(msg):
    answer = []
    dic = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))
    w = 0
    cnt = 26
    n = len(msg)
    # 맨 마지막에, dic에 없는 문자열이 있어야만 if문에 걸려서 while이 종료 가능
    msg += ' '
    while w < n:
        # 최소 w번째 index는 dic에 존재 -> w~w+1이 dic에 없으려면, msg[w:w+2]
        for c in range(w+2, n+2):
            if msg[w:c] not in dic:
                answer.append(dic[msg[w:c-1]])
                cnt += 1
                # 사전에 추가
                dic[msg[w:c]] = cnt
                # w 갱신
                w = c-1
                break
                
    return answer


# 다른 사람 풀이
## 1. 제일 깔끔한듯: 테스트 14 〉	통과 (1.33ms, 10.2MB)
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer

## 2. chr 활용. 제일 빠름: 테스트 14 〉	통과 (0.52ms, 10.4MB)
def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp:
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer


'''
# Result
풀이 시간: 30분
## 1. 테스트 14 〉통과 (114.89ms, 10.2MB) 
## 2. 테스트 15 〉통과 (0.84ms, 10.4MB)
'''