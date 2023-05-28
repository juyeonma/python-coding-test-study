# 전에 풀었던 문제..
# max를 이용해서 점화식을 세우면 되는 것 같다.

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    # dp = [0] * n
    # dp[0] = max(sticker[0][0], sticker[1][0])
    # if n >= 1:
    #     dp[1] = max(sticker[0][0] + sticker[1][1], sticker[1][0] + sticker[0][1])
    
    # 결국 전에 푼 거 봤다..
    # 다시 풀어도 모르면 어떻게 하지........

    if n > 1:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]

    if n > 2:
        for j in range(2, n):
            sticker[0][j] += max(sticker[1][j-1], sticker[1][j-2])
            sticker[1][j] += max(sticker[0][j-1], sticker[0][j-2])
    print(max(sticker[0][n-1], sticker[1][n-1]))

# 메모리 : 47876KB 시간 : 768ms