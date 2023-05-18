'''
# 백준_1912_연속합. 실버 2. 풀이: 23.05.18

# How to
- 모든 수의 합의 최솟값은 자기 자신.
- 점화식
dp[n] = max(dp[n-1]+dp[n], dp[n])

# Review
- 역시나 바텀업으로 계속 풀게된다. 탑다운으로도 풀어봐야지.
'''

# Code
import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    # dp[i] = max(dp[i-1]+dp[i], dp[i])와 같다.
    if 0 < dp[i-1]:
        dp[i] = dp[i-1]+dp[i]
        
print(max(dp))        

'''
# Result
풀이 시간: 15분
메모리: 38964 KB
시간: 72 ms
코드 길이: 191 B
'''