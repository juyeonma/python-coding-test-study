'''
# 백준_10844_쉬운 계단수. 실버 1. 풀이: 23.08.02

# How to
- 끝자리에서 1을 빼거나, 1을 더하면 1씩 차이난다. 즉 2배로 증가
...1 + 0 or 2
- but 0, 9는 맨 끝 수라서, 1개만 증가
...0 + 1
...9 + 8

- 점화식:
i: 수의 길이, j: 끝자리 수
수의 길이가 i일 때, 끝자리 j인 수의 개수:
dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# Review
- 풀이 시간: 1시간
- 되게 간단한 문제인데도 불구하고 규칙 찾는데 조금 헤맸다..
- 그런데 탑다운으로는 왜 실패했을까? -> i < 1, 즉 수의 길이가 0일 때를 추가하니, 성공했다.
'''

# Code
# 1. Bottom-Up: 성공
## 메모리: 31256 KB, 시간: 44 ms
n = int(input())

# 9+1=10, 0-1=-1 -> 둘다 가능한 수가 0, 즉 불가능해야한다.
# dp[i][10] = dp[i][-1] = 0
dp = [[0] * 11 for _ in range(n+1)]
dp[1][1:10] = [1] * 9

for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1]) % 1_000_000_000)


# 2. Top-Down: 실패 -> i < 0 조건 추가 후 성공
## 메모리: 31256 KB, 시간: 40 ms
n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
dp[1][1:] = [1] * 9

def solve(i, j):
    if i < 1 or j < 0 or j > 9:
        return 0
    
    if dp[i][j]:
        return dp[i][j]
    
    dp[i][j] = solve(i-1, j-1) + solve(i-1, j+1)

    return dp[i][j]

for j in range(10):
    solve(n, j)

print(sum(dp[-1]) % 1_000_000_000)