'''
# 프로그래머스_순위 검색. Lv 2. 풀이: 23.06.14 -> 실패

# How to
## 나의 풀이
- 정렬 후 하나씩 탐색하며 조건에 맞는지 찾기 
    - 당연하게도, 효율성 테스트에서 시간초과
    
    
## 카카오 풀이(아래 모범답안)
- 출처: https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/#문제-3-순위-검색
- 참고: https://velog.io/@dogcu/프로그래머스-순위-검색
    
- 모든 경우의 수(16가지)를 key, 점수를 value로 딕셔너리에 넣는다.
- 조건을 key로 해서 value를 찾고, 그 점수들을 이분 탐색(Binary Search)으로 찾는다
- 이때 Lower Bound(원하는 값 이상이 처음 나오는 위치를 찾는 과정)을 이용한다.
    
    
# Review
- 딕셔너리를 사용하려고 했는데..생각보다 복잡하다.
    - 이중 딕셔너리를 쓴다면..?
- 아무리 해도 효율성을 통과 못해서, 결국 검색 하였다.
    - 딕셔너리를 사용해야겠다고 생각했지만, 모든 점수를 value로 넣을 생각은 못하였다. 그리고 이분 탐색을 이용할 생각도..
- 이런 사소한 생각의 차이가 정답을 가르나 보다..
'''


# 1. 실패 Code
def solution(info, query):
    answer = []
    n = len(info)
    info.sort()
    idx = {'cpp': [False, n], 'java': [False, n], 'python': [False, n]}

    for i in range(n):
        tmp = info[i].split()[0]
        if not idx[tmp][0]:
            idx[tmp][0] = i
            
    if idx['cpp'][0]:
        idx['cpp'][1] = min(idx['java'][0], idx['python'][0])
            
    if idx['java'][0]:
        idx['java'][1] = idx['python'][0]
        
    for q in query:
        # a, b, c, d, e
        b, c, d = True, True, True
        lang, _, job, _, career, _, food, score = q.split()

        if job == 'frontend':
            b = False
        if career == 'senior':
            c = False
        if food == 'pizza':
            d = False
            
        # 더 어떻게 구현하지..?..
        
    return answer


# 2. 시간초과 Code
## 정확성 테스트 9 〉통과 (246.28ms, 13.2MB), 효율성 테스트 전부 시간초과
def solution(info, query):
    answer = []
    info = [i.split() for i in info]
    # 점수로 내림차순
    info.sort(key=lambda x: -int(x[-1]))

    for question in query:
        question = question.replace('and', '').split()
        cnt = 0
        for person in info:
            # 원하는 점수보다 낮다면, break
            if int(question[-1]) > int(person[-1]):
                break
                
            for i in range(4):
                if question[i] == '-':
                    continue
                # 원하는 정보와 다르다면, break
                if question[i] != person[i]:
                    break
            # 모든 정보가 일치한다면, +1
            else:
                cnt += 1
                
        answer.append(cnt)
        
    return answer


# 3. 시간초과 Code
## 정확성 테스트 9 〉통과 (261.31ms, 13.9MB), 효율성 테스트 전부 시간초과
def solution(info, query):
    answer = []
    info = [i.split() for i in info]
    dic = {}

    for question in query:
        question = question.replace('and', '').split()
        # '-' 가 아닌 index만 모아서
        idx = tuple(i for i, c in enumerate(question) if c != '-')
        
        # 이전에 정렬한 적 없다면, 정렬
        if idx not in dic:
            dic[idx] = sorted(info, key=lambda x: [x[i] for i in idx])

        cnt = 0
        flag = False
        for person in dic[idx]:      
            # 원하는 점수보다 낮다면, 넘어감
            if int(question[-1]) > int(person[-1]):
                continue

            for i in range(4):
                if question[i] == '-':
                    continue
                # 원하는 정보와 다르다면, break
                if question[i] != person[i]:
                    break
            # 모든 정보가 일치한다면, +1
            else:
                # 다른 종류값이 나오면 살펴볼 필요가 없도록
                flag = True
                cnt += 1
                continue
            
            # 이미 4가지 정보가 일치했었는데, 다른 정보가 나왔다면 살펴볼 필요 없음
            if flag:
                break

        answer.append(cnt)
        
    return answer


# 모범 답안
# 1. 점수배열들의 정렬을 어디서 해주느냐도 중요합니다.
# 출처: https://school.programmers.co.kr/questions/49124
## 정확성 테스트 10 〉통과 (44.91ms, 15.8MB)
## 효율성 테스트 3 〉통과 (737.54ms, 96.6MB)
from collections import defaultdict
from itertools import product
from bisect import bisect_left

def solution(info, query):
    info = [tuple(e.split(" ")) for e in info]
    queries = [tuple(e for e in q.split(" ") if e != 'and') for q in query]

    scores = defaultdict(list)
    for entry in info:
        for record in product(*tuple(('-', e) for e in entry[:-1])):
            scores[record].append(int(entry[-1]))
    for record in scores:
        scores[record].sort()

    output = []
    for query in queries:
        record, score = query[:-1], int(query[-1])
        output.append(len(scores[record]) - bisect_left(scores[record], score))
    return output


'''
# Result
풀이 시간: 실패
'''