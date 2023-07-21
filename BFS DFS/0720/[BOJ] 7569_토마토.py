import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
boxes = []
for _ in range(h):
    tomato = []
    for _ in range(n):
        t = list(map(int, input().split()))
        tomato.append(t)
    boxes.append(tomato)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]
def bfs():
    while q:
        k, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nk = k + dk[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or nk < 0 or nk >= h:
                continue
            if boxes[nk][nx][ny] == 0:
                boxes[nk][nx][ny] = boxes[k][x][y] + 1
                q.append((nk, nx, ny))

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                q.append((i, j, k))

bfs()
flag = False
max_value = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 0:
                flag = True
        max_value = max(max_value, max(boxes[i][j]))
    if flag:
        print(-1)
        sys.exit(0)
print(max_value-1)

# 그냥 단순하게 이중포문부분을 => 삼중포문으로 바꿔서 구현
# 주어진 수가 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100이므로 시간 복잡도가 통과될 것 같았음!