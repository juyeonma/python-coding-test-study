# bfs 풀기..
# 오 대박... 이거는.. 풀기는 했습니다..ㅠㅠ..
# 그래도 bfs는 기억을 하나봐요...
from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count
max_value = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j]= 0
            max_value = max(bfs(i, j), max_value)
print(max_value)