'''
# 백준_9251_LCS. 골드 5. 풀이: 23.05.21

# How to
- 두 문자열을 전부 순차적으로 탐색하여, 매번 최댓값을 기록한다.
    - 만약 같은 알파벳이면, 이전 값에 1을 더하여 기록한다.
    dp[i][j] = dp[i-1][j-1] + 1
    - 만약 다르다면, 이전의 값 중 최댓값으로 기록한다.
    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# Review
- 비교적 쉬운 문자였다. 그냥 탐색하기만 하면 되니까..
- 다만 dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 이 부분이 조금 헷갈리긴 했다.
- 다만 심플한 코드에 비해 메모리와 시간이 크다. 더 효율적으로 줄여볼까?
'''

# Code
import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
aa, bb = len(a)+1, len(b)+1

# 이전값과 비교하다보니, dp[0] 이 나올 수 있기 때문에 0칸을 비워둠
dp = [[0]*(bb) for _ in range(aa)]

for i in range(1, aa):
    for j in range(1, bb):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
print(dp[-1][-1])


'''
# Result
풀이 시간: 10분
메모리: 55712 KB
시간: 548 ms
코드 길이: 451 B
'''