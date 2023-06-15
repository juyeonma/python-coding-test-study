# 풀이 시간 : 50분

# 효율성 : 0점 => 시간복잡도를 고려하지 않음

import re
def solution(info, query):
    answer = []
    for q in query:
        q = re.sub('and', '', q).split()
        cnt = 0
        for i in info:
            i = i.split()
            lan, job, career, food, score = i[0], i[1], i[2], i[3], i[4]
            if lan != q[0] and q[0] != '-':
                continue
            if job != q[1] and q[1] != '-':
                continue
            if career != q[2] and q[2] != '-':
                continue
            if food != q[3] and q[3] != '-':
                continue
            if score < q[4]:
                continue
            cnt += 1
        answer.append(cnt)    
    return answer
solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])

# dictionary로 풀었어야 했나..?!..
# => lower bound를 사용해야한다고 한다.(이분 탐색..)
# 이분 탐색에 자신 있다 생각했는데..아니었나보다..ㅎ
# 코드 참고 : https://velog.io/@dogcu/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89
# bisuect_left => lower bound
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score) 

    for value in dic.values():
        value.sort()   

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)      
    return answer

# lower bound 구현 코드
from itertools import combinations
from collections import defaultdict

def lower_bound(begin, end, target_list, target):
    if begin >= end:
        return begin    
    mid = (begin + end) // 2
    if target_list[mid] >= target:
        return lower_bound(begin, mid, target_list, target)
    else:
        return lower_bound(mid+1, end, target_list, target)

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score) 

    for value in dic.values():
        value.sort()   

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = lower_bound(0, len(target_list), target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)          
    return answer

# 다시 풀기!!!!!!!!