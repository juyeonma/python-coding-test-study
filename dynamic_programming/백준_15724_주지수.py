'''
# 백준_15724_주지수. 실버 1. 풀이: 23.08.04

# How to
1. dp: 누적 합 구하기
-  dp[i][j]: (0, 0) ~ (i, j) 까지 인구 합.
- A와 B의 합집합 = 집합 A + 집합 B - A와 B의 교집합
- 즉 누적으로 더하면서, 중복(dp[i-1][j-1])은 빼주고 현재 좌표의 값을 더한다.
- 점화식: 
dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + dp[i][j]

2. (x1, y1) ~ (x2, y2) 의 합: 직사각형 구하기
- 시작 좌표가 0, 0 이면 그냥 끝 좌표의 dp값을 출력한다.
- 시작 좌표가 중간 좌표면, 전체 배열을 사등분하여 셈한다.   
    - 구하려는 직사각형이 4라면, (1+2+3+4) - ((1+2)+(1+3)) + 1
1 2
3 4

- 점화식: 
dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1]) + dp[x1-1][y1-1]


# Review
- 풀이 시간: 1시간
- 바텀업에서 인덱스를 벗어나는 경우가 발생하므로 별도로 처리했더니, 코드가 조금 길어졌다.
- 그래서 탑다운을 해봤지만, 재귀 깊이도 너무 깊고 느렸다.
'''

# Code
# 1. Bottom-Up: 성공
## 메모리: 73224 KB, 시간: 884 ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# dp[i][j]: (0, 0) ~ (i, j) 까지 인구 합.
dp = [list(map(int, input().split())) for _ in range(n)]

# 0행
for j in range(1, m):
    dp[0][j] += dp[0][j-1]

# 0열
for i in range(1, n):
    dp[i][0] += dp[i-1][0]

# 1행 1열부터 ~ 끝까지
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# (x1, y1) ~ (x2, y2) 의 합: 직사각형 구하기
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    if x1 > 0 and y1 > 0:
        print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1]) + dp[x1-1][y1-1])
        
    elif x1 > 0:
        print(dp[x2][y2] - dp[x1-1][y2])
    
    elif y1 > 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    
    # (x1, y1) == (0, 0)
    else:
        print(dp[x2][y2])


# 2. Top-Down: 성공, 그러나 너무 느림
## 메모리: 81528 KB, 시간: 4020	ms
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: (0, 0) ~ (i, j) 까지 인구 합.
dp = [[0]*m for _ in range(n)]
def sum_dp(i, j):
    if i < 0 or j < 0:
        return 0
    
    if dp[i][j]:
        return dp[i][j]
    
    dp[i][j] = sum_dp(i-1, j) + sum_dp(i, j-1) - sum_dp(i-1, j-1) + board[i][j]
    
    return dp[i][j]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    
    # (x1, y1) ~ (x2, y2) 의 합: 직사각형 구하기
    print(sum_dp(x2, y2) - (sum_dp(x1-1, y2) + sum_dp(x2, y1-1)) + sum_dp(x1-1, y1-1))
