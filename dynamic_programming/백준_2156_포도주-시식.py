'''
# 백준_2156_포도주 시식. 실버 1. 풀이: 23.07.31

# How to
- 규칙
    - 1. i번째 포도주를 선택하면, wine[i] = 0
    - 2. 3연속은 안된다 = 2연속까지는 가능하다.
    
- 점화식: 
    - n번째를 안 마신다면, n-1번째에 마셨든 안 마셨든 연속 3잔 금지 규칙을 준수.
    - dp[n][0] = max(dp[n-1])
1 1 0
1 0 0
0 0 0

    - n번째를 마신다면, n-1번째에 안 마신건 괜찮지만, n-1번째에 마신건 연속 3잔 금지 규칙이 위험해짐.
    - 즉 n-2번째에 안 마셨는데 n-1번째에 마신 조건에서만 n번째를 마실 수 있음.
    - dp[n][1] = max(dp[n-1][0], dp[n-2][0] + wine[n-1]) + wine[n]
0 0 1
0 1 1
1 0 1


# Review
- 풀이 시간: 20분
'''

# Code
# 1. 성공
## 메모리: 32568 KB, 시간: 56 ms
import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [[0, 0] for _ in range(n)]

dp[0][1] = wine[0]

if n > 1:
    dp[1] = [wine[0], wine[0]+wine[1]]
    
for i in range(2, n):
    # n번째를 안 마신다면
    dp[i][0] = max(dp[i-1])
    # n번째를 마신다면
    dp[i][1] = max(dp[i-1][0], dp[i-2][0] + wine[i-1]) + wine[i]
    
print(max(dp[n-1]))


# dp를 딕셔너리로 했을때 메모리와 시간이 같았다: 32568 KB, 시간: 56 ms
# import sys
# input = sys.stdin.readline

# n = int(input())
# wine = [int(input()) for _ in range(n)]

# dp = {0: [0, wine[0]]}

# if n > 1:
#     dp[1] = [wine[0], wine[0]+wine[1]]

# for i in range(2, n):
#     dp[i] = [max(dp[i-1]), max(dp[i-1][0], dp[i-2][0] + wine[i-1]) + wine[i]]
    
# print(max(dp[n-1]))