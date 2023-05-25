# def fibonacci(n):
#     global count
#     count += 1
#     if n < 2:
#         return n
#     return fibonacci(n-2) + fibonacci(n-1)

# n = int(input())
# count = 0
# fibonacci(n)
# print(count % 1000000007)
# 73%?!에서 시간초과.. => 점화식으로 풀어야하는것같다..

# 0 1 2 3 4  5  6  7
# 1 1 3 5 9 15 25 41
#  +2 +2 +4 +6 +10 +16
# dp[i] = dp[i-1] + (dp[i-1]-dp[i-2]) + (dp[i-2]-dp[i-3])

n = int(input())
dp = [0] * (n+1)

dp[0] = 1
if n >= 1:
    dp[1] = 1

if n >= 2:
    dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + (dp[i-1]-dp[i-2]) + (dp[i-2]-dp[i-3])) % 1000000007

print(dp[n])

# 메모리 : 31256KB 시간 : 40ms