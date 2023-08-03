'''
# 백준_1520_내리막 길. 골드 3. 풀이: 23.07.29 -> 실패

# How to
- i, j가 상하좌우보다 낮은 지점일 때,
dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i][j+1] + dp[i+1][j]

# Review
- 풀이 시간:
- 상하좌우를 살펴서 현재가 더 낮을 경우, dp를 갱신해야한다. 
    - 그런데 미래의 좌표, 즉 아직 탐색하지 않은 좌표의 값은 0인데, 어떻게 갱신하지?ㄴ
- 단순히 위와 왼쪽, 즉 이전 좌표만 탐색하기에는 예제처럼 오른쪽이나 아래에서 이동할 수도 있다..

- 혹시 몰라서 dfs와 bfs로도 해봤지만, 역시나 실패.
'''

# Code
# 1. DP
# 상하좌우를 탐색할 때, 그 다음 좌표를 이번 좌표로 어떻게 갱신하지?
#
#

# 2. dfs: 시간초과
## 메모리:  KB, 시간:  ms
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]

answer = 0
def dfs(x, y):
    global answer
    if (x, y) == (n-1, m-1):
        answer += 1
        return
    
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    
    for i, j in zip([1,-1,0,0], [0,0,1,-1]):
        nx, ny = x + i, y + j
        if nx < 0 or nx >= n or ny < 0 or ny >= m or board[x][y] <= board[nx][ny]:
            continue
        dfs(nx, ny)
        
dfs(0, 0)
print(answer)


# 3. bfs: 실패
## 메모리:  KB, 시간:  ms
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dp[0][0] = 1
visited[0][0] = True

def bfs():
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for i, j in zip([1,-1,0,0], [0,0,1,-1]):
            nx, ny = x + i, y + j
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[x][y] <= board[nx][ny]:
                continue
            
            q.append((nx, ny))
            if not visited[nx][ny]:
                dp[nx][ny] += dp[x][y]
                visited[nx][ny] = True
                continue
            dp[nx][ny] += 1
                                                          
bfs()
print(dp[-1][-1])
