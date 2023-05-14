# 최소 거리 => bfs
# 아기 상어2 응용하면 된다!
# 1. 이동할 수 있는 거리는 다 계산
# 2. 목적지에 해당하는 거리 출력
# 메모리 : 34140KB
# 시간 : 2324ms

# 시간이 오래걸렸다
# 왜?
# 갈 수 있는 이동 거리는 다 출력했기 때문에.. => BFS가 아니라 DFS인가..? 헷갈림..ㅠ
# 목적지에 도착하면 종료하는 코드를 넣었으면 됐을 것 같다..!
# => 목적지와 같아지면 종료되게 코드를 짜봤더니 답이 달라졌다..(나중에 다른 사람들 코드를 봐야겠다..)
import sys
from collections import deque
input = sys.stdin.readline

# 나이트가 이동할 수 있는 거리
dx = [-1, -2, 1, 2, -2, -1, 2, 1]
dy = [-2, -1, -2, -1, 1, 2, 1, 2]

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                    continue
            if matrix[nx][ny] == 0:
                q.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1

t = int(input())
q = deque()
for _ in range(t):
    l = int(input())
    matrix = list([0] * l for _ in range(l))
    start_x, start_y = map(int, input().split())
    matrix[start_x][start_y] = 1
    end_x, end_y = map(int, input().split())
    q.append((start_x, start_y))
    bfs()
    print(matrix[end_x][end_y]-1)