'''
# 프로그래머스_[3차] 압축. Lv 2. 풀이: 23.06.08

# How to
- w와 c의 인덱스를 조정해가면서, 딕셔너리에 존재하는지 탐색한다.
- w: 0부터 시작, c: 반복문에서 맨 끝 인덱스부터 거꾸로.
    - 딕셔너리에 존재하는 문자열을 찾으면, c가 새로운 w가 된다.

# Review
- for문에서 범위 때문에 조금 헤맸는데, 과정 자체가 어렵지는 않았다.
- 예전에 비슷한 문제를 풀었던거 같기도 하고..
- 다만 다른 사람 풀이에 비해서 시간이 매우매우 많이..걸렸다..
    - chr을 배웠다. 
'''

# 성공 Code
def solution(msg):
    answer = []
    dic = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))
    w = 0
    cnt = 26
    n = len(msg)
    while w < n:
        for c in range(n, w, -1):
            if msg[w:c] in dic:
                answer.append(dic[msg[w:c]])
                cnt += 1
                dic[msg[w:c+1]] = cnt
                w = c
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

## 2. chr 활용. 제일 빠름: 테스트 14 〉	통과 (0.60ms, 10.3MB)
def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
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
테스트 14 〉통과 (114.89ms, 10.2MB)
'''