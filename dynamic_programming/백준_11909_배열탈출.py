'''
# 백준_11909_배열탈출. 골드 5. 풀이: 23.08.06

# How to
- 내림차순으로 이동
- dp에 이동하는 두 좌표간의 차이+1 만큼 지출을 누적시킨다.
- 점화식:
i, j에서의 값은 i-1, j 에서 오거나 or i, j-1에서 오는 것 중 최솟값
dp[i][j] = min(dp[i-1][j]+(board[i][j]-board[i-1][j]+1)*(board[i][j] >= board[i-1][j]),
                dp[i][j-1]+(board[i][j]-board[i][j-1]+1)*(board[i][j] >= board[i][j-1]))

# Review
- 풀이 시간: 30분
- 생각보다 단순한 문제였다.
'''

# Code
# 1. 성공
## 메모리: python3: 266392 KB, 시간: 4992 ms, pypy3: 203624 KB, 시간: 1072 ms
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

def cost(x1, y1, x2, y2):
    # 내림차순이 아닐 경우, 버튼을 누르고 돈을 지불함
    if board[x1][y1] >= board[x2][y2]:
        return board[x1][y1] - board[x2][y2]+1
    
    # 내림차순일 경우, 버튼 안 누름
    return 0
    
def solve(i, j):
    # 0행 0열은 0
    if (i, j) == (0, 0):
        return 0
    
    # 0행 또는 0열일 때,
    elif i == 0:
        return dp[0][j-1] + cost(0, j, 0, j-1)
        
    elif j == 0:
        return dp[i-1][0] + cost(i, 0, i-1, 0)
    
    # 1행 1열 이후일 때,    
    else:
        return min(dp[i-1][j]+cost(i, j, i-1, j), dp[i][j-1]+cost(i, j, i, j-1))

for i in range(n):
    for j in range(n):
        dp[i][j] = solve(i, j)
        
print(dp[-1][-1])