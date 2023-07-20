import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

graph = []
min_value = int(1e9)
max_value = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(min(data), min_value)
    max_value = max(max(data), max_value)
    graph.append(data)

# dfs 풀이
def dfs(x, y):
    if 0 <= x < n and 0 <= y < n:
        if not visit[x][y]:
            visit[x][y] = True

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

def check(x):
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= x:
                visit[i][j] = True
result = 0

for i in range(min_value-1, max_value+1):
    count = 0
    visit = [[False] * n for _ in range(n)]
    check(i)
    for x in range(n):
        for y in range(n):
            if not visit[x][y]:
                count += 1
                dfs(x, y)
    result = max(result, count)
print(result)

# 	메모리 : 32500	시간 : 2368ms

# bfs 풀이
def bfs():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue

            if not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx, ny))
q= deque()
result = 0

for i in range(min_value-1, max_value+1):
    count = 0
    visit = [[False] * n for _ in range(n)]
    check(i)
    for x in range(n):
        for y in range(n):
            if not visit[x][y]:
                count += 1
                q.append((x, y))
                bfs()
    result = max(result, count)
print(result)

# bfs 풀이 메모리 : 34208	시간 : 708ms