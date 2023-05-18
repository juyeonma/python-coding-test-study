'''
# 백준_1149_RGB거리. 실버 1. 풀이: 23.05.18

# How to
- dp[n-1] != dp[n] != dp[n+1]
- 점화식
    - 현재 색이 직전 색과 다르면 된다.
    - 즉, 현재색을 고정하고 이전 비용의 최솟값 + 현재색 = 현재색의 비용
dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + color[n][0]
dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + color[n][1]
dp[n][2] = min(dp[n-1][0], dp[n-1][1]) + color[n][2]


# Review
- 바텀업 방식이 쉽게 느껴진다. 탑다운은 어떻게 하면 좋을까..?
'''

# Code
import sys
input = sys.stdin.readline

n = int(input())
# 빨강, 초록, 파랑으로 칠하는 비용
color = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = color[0]
        
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + color[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + color[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + color[i][2]

print(min(dp[n-1]))


'''
# Result
풀이 시간: 10분
메모리: 31256 KB
시간: 40 ms
코드 길이: 438 B
'''