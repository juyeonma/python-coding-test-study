import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[1] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0

result = []
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                count += 1
                graph[nx][ny] = 0
                q.append((nx, ny))
    return count
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
            graph[i][j] = 0
            result.append(bfs())

result.sort()
print(len(result))
print(*result)

# 	메모리 : 34160	시간 : 72ms