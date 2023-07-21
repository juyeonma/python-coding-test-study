# 시간초과 코드..
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(n))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

def melt(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            continue
        if data[nx][ny] == 0:
            count += 1
    da[x][y] = max(data[x][y] - count, 0)

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx, ny))
i = 0
while True:
    visit = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if not data[x][y]:
                visit[x][y] = True
    result = 0
    for x in range(1, n-1):
        for y in range(1, m-1):
            if not visit[x][y]:
                q.append((x, y))
                bfs()
                result += 1
    if result >= 2:
        print(i)
        break
    if result == 0:
        print(0)
        break
    da = [[0] * m for _ in range(n)]
    for x in range(1, n-1):
        for y in range(1, m-1):
            if data[x][y]:
                melt(x, y)
    data = da
    i += 1

# 시간 통과 코드..
# 참고 : https://wookcode.tistory.com/155
import collections

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = collections.deque()
day = 0
check = False

def bfs(a,b):
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

# 빙산이 분리될때까지 돌아줌
while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))
    # 빙산을 깍아줌           
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    if len(result) == 0: # 빙산이 다없어질때까지 분리가 되지않으면 break
        break
    if len(result) >= 2: # 빙산이 분리되면 break
        check = True
        break
    day += 1

if check:        
    print(day)
else:
    print(0)