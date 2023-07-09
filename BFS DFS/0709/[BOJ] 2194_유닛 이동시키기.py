from collections import deque
n, m, a, b, k = map(int, input().split())
data = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    data[x-1][y-1] = 0
    visit[x-1][y-1] = True

s_x, s_y = map(int, input().split())
e_x, e_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
q.append((s_x-1, s_y-1))
visit[s_x-1][s_y-1] = True
def check(x, y):
    if 0 > x or x >= n or 0 > y or y >= m or visit[x][y] == True:
        return False
    
    for i in range(x, x+a):
        if 0 > i or i >= n:
            return False
        for j in range(y, y+b):
            if 0 > j or j >= n:
                return False
            if data[i][j] == 1:
                return False
    return True

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if check(nx, ny):
                data[nx][ny] = data[x][y] + 1
                visit[nx][ny] = True
                q.append((nx, ny))

bfs()
num = data[e_x-1][e_y-1]
if num:
    print(data[e_x-1][e_y-1])
else:
    print(-1)

# 어디가 틀린거지.....ㅜㅜ