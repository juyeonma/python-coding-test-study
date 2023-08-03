'''
# 백준_14567_선수과목. 골드 5. 풀이: 23.08.03

# How to
- 어떤 과목 최소수강학기 = 그 과목의 선수과목들의 최소 수강학기 중 최댓값 + 1
- 점화식
i의 선수과목 리스트: [j1, j2, j3..]
dp[i] = max(dp[j1], dp[j2], dp[j3], ...) + 1

- 예시
5의 선수과목: 2, 4
1 -> 3 -> 4 : 3학기
1 -> 2: 2학기m
1 -> 2, 3 -> 4 -> 5: 4학기

# Review
- 풀이 시간: 30분
- a, b로 주어지는 입력을 과목: 선수과목 리스트 담는 것 말고, a b 순서 그대로 담으면 어떨까?
- 매번 dp값을 선수과목들의 dp 값 중 최댓값으로 갱신하는데, 여기서 시간이 많이 소요되는 듯 하다..
'''

# Code
# 1. 성공
## 메모리: 44288 KB, 시간: 532 ms
import sys
input = sys.stdin.readline

# 과목 수 n, 선수 조건의 수 m
n, m = map(int, input().split())

# 과목: 선수과목 리스트
prerequisite = [[] for _ in range(n+1)]

for _ in range(m):
    # a: b의 선수과목. 즉 a -> b 순서로 수강해야한다.
    a, b = map(int, input().split())
    prerequisite[b].append(a)
    
# 최소 1학기는 수강해야함
dp = [1] * (n+1)

for b in range(1, n+1):
    # b의 선수과목이 존재한다면,
    if prerequisite[b]:
        # b의 dp값 = b의 선수과목들의 dp값 중 최댓값 + 1
        dp[b] += max(map(lambda a: dp[a], prerequisite[b]))
        
print(*dp[1:])


