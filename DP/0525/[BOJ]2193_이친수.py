# 점화식
# 1 2 3 4 5
# 1 1 2 3 5
# dp[i] = dp[i-2] + dp[i-1]
n = int(input())
dp = [0] * (n+1)
dp[1] = 1
if n >= 2:
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n])

# 메모리 : 31388KB	시간 : 40ms