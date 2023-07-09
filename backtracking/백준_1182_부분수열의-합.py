'''
# 백준_1182_부분수열의 합. 실버 2. 풀이: 23.07.06

# How to
- 하나씩 원소를 탐색하는데,
    - 현재 원소까지 더한 값이 s라면, 정답 +1
- 재귀로 들어가는데,
    - 현재(idx) 원소를 빼고 그 다음 원소 탐색
    - 현재(idx) 원소를 더한 채로 그 다음 원소 탐색
    
- 처음에는 수열의 합이 0, 현재 원소는 0번째 인덱스로 시작.


# Review
- 무난하게 푼거 같은데, 맞힌 사람 풀이를 보니 다들 백트래킹이 아닌거 같다..?
'''

# 1. 조합으로 풀기: 성공: 352 ms
from itertools import combinations
n, s = map(int, input().split())
num = list(map(int, input().split()))
answer = 0

for i in range(1, n+1):
    for j in combinations(num, i):
        if sum(j) == s:
            answer += 1

print(answer)


# 2. 백트래킹으로 풀기: 성공: 272 ms
def backtracking(num, now, idx, n):
    global answer
    
    # 범위를 벗어났으면, return
    if idx >= n:
        return

    # 현재(idx) 원소를 더한 수열
    now += num[idx]
    # 현재 수열의 합이 s라면,
    if now == s:
        answer += 1
            
    # 현재(idx) 원소를 빼고 그 다음 원소 탐색
    backtracking(num, now-num[idx], idx+1, n)
    # 현재(idx) 원소를 더한 채로 그 다음 원소 탐색
    backtracking(num, now, idx+1, n)
    
n, s = map(int, input().split())
num = list(map(int, input().split()))

answer = 0
backtracking(num, 0, 0, n)

print(answer)


'''
# Result
풀이 시간: 20분
메모리: 31256 KB
시간: 272 ms
코드 길이: 543 B
'''