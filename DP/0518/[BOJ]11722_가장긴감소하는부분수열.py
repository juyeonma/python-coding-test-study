# 이중 포문이 가능했는데 염두해두지 않았다..
# 앞으로 주어진 수의 크기와 시간 복잡도에 대해서 먼저 생각하고 문제를 풀어야겠다

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().rstrip().split()))

dp = [1] * n

# dp[0] = 1

# for i in range(1, n):
#     if data[i-1] > data[i]:
#         dp[i] = dp[i-1]+1
#     else:
#         dp[i] = dp[i-1]
# 반례 : 6 / 20 10 20 10 20 10


# 참고 : https://www.acmicpc.net/board/view/102791
for i in range(n):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))