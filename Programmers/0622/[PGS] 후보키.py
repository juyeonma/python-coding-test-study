# relation의 컬럼(column)의 길이는 1 이상 8 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
# relation의 로우(row)의 길이는 1 이상 20 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
# => 숫자가 완전 적음
# 유형 : 완전탐색..?

# 실패..
# 채점 결과 (18, 19, 20, 25, 28 실패) => 질문하기 참고 https://school.programmers.co.kr/questions/16502
# 정확성: 82.1
# 합계: 82.1 / 100.0
from itertools import combinations
def solution(relation):
    answer = []
    com = []
    count = 0
    for i in range(len(relation[0])):
        column = []
        for j in range(len(relation)):
            column.append(relation[j][i])
        if len(column) != len(set(column)):
            answer.append(column)
            com.append(i)
        else:
            count += 1
    comb = []
    for i in range(2, len(com)+1):
        for j in combinations(range(len(com)), i):
            sub = []
            flag = False
            for k in comb:
                if set(k) & set(j) == set(k):
                    flag = True
            if flag:
                break
            for x in range(len(answer[0])):
                s = []
                for y in j:
                    s.append(answer[y][x])
                sub.append(s)
            if len(sub) == len(set(map(tuple, sub))): # 이중리스트 set하는 법
                comb.append(j)
                count += 1
    return count

# 문제점 찾고 보완
# 문제점
# 최소성을 가졌을 때 for문을 종료했다. => 종료가 아닌 다음 for문으로 continue 해줬어야 했다.

from itertools import combinations
def solution(relation):
    answer = []
    count = 0
    for i in range(len(relation[0])):
        column = []
        for j in range(len(relation)):
            column.append(relation[j][i])
        if len(column) != len(set(column)):
            answer.append(column)
        else:
            count += 1
    comb = []
    for i in range(2, len(answer)+1):
        for j in combinations(range(len(answer)), i):
            sub = []
            flag = False
            for k in comb:
                if set(k) & set(j) == set(k):
                    flag = True
            if flag:
                continue
            for x in range(len(answer[0])):
                s = []
                for y in j:
                    s.append(answer[y][x])
                sub.append(s)
            if len(sub) == len(set(map(tuple, sub))):
                comb.append(j)
                count += 1
    return count
# solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']])

# 속도
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 24 〉	통과 (3.74ms, 10.2MB)