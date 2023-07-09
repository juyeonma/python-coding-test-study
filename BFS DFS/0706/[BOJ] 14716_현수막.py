from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

# bfs로 구현
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

count = 0
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
            graph[i][j] = 0
            bfs()
            count += 1
print(count)

# 메모리 : 34128	시간 : 156ms

# dfs 구현..
sys.setrecursionlimit(10**6)
def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(i, j)
            count += 1
print(count)
# 	메모리 : 43880	시간 : 220ms