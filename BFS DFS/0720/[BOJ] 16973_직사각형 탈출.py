# 전에 풀었던 문제랑 비슷한 문제였다..!
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
visited = [[False] * m for _ in range(n)]
h, w, sr, sc, fr, fc = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def check(x, y):
    if 0 > x or x >= n or 0 > y or y >= m or visited[x][y] or graph[x][y] != 0:
        return False
    for i in range(h*w):
        nx = i % h + x
        ny = i // w + y
        if 0 > nx or nx >= n or 0 > ny or ny >= m or graph[nx][ny] == 1:
            return False
    return True

def dfs():
    while q:
        x, y = q.popleft()
        if x == fr-1 and y == fc-1:
            return -graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if check(nx, ny):
                graph[nx][ny] = graph[x][y]-1
                q.append((nx, ny))
                visited[nx][ny] = True
    return -1
q = deque()
visited[sr-1][sc-1] = True
q.append((sr-1, sc-1))
print(dfs())


# 시간 초과..ㅠㅠ.......
# 어떻게 시간을 줄일지부터 생각을 못했다...


# 통과 코드
# 참고 : https://reliablecho-programming.tistory.com/122
from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
visited = [[False] * M for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 시간초과를 막기 위해 미리 벽을 저장해둔다.
walls = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            walls.append((i, j))

# 저장해둔 벽이 직사각형 범위 내에 있다면 False를 반환
def check(i, j):
    for w_row, w_col in walls:
        if i <= w_row < i+H and j <= w_col < j+W:
            return False
    return True


def bfs():
    q = deque()
    q.append((Sr - 1, Sc - 1, 0))

    while q:
        y, x, cnt = q.popleft()
        visited[y][x] = True

        if y == Fr-1 and x == Fc-1:
            print(cnt)
            return

        for l in range(4):
            yy = dy[l] + y
            xx = dx[l] + x
            # 직사각형 범위계산
            if 0 <= yy < N and 0 <= xx < M and 0 <= yy + H - 1 < N and 0 <= xx + W - 1 < M:
                if not visited[yy][xx]:
                    if check(yy, xx):
                        visited[yy][xx] = True
                        q.append((yy, xx, cnt+1))

    print(-1)
    return

bfs()

# 저렇게 간단하게 check 부분을 생각하는게 키포인트였던것 같다