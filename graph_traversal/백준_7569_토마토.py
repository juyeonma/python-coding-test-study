'''
# 백준_7569_토마토. 골드 5. 풀이: 23.07.20

# How to

- 익은 토마토의 인접한 안 익은 토마토는 익게 됨
    - 인접한 여섯 방향: 위, 아래, 왼쪽, 오른쪽, 앞, 뒤

- BFS
    - 단지 z축이 추가된 것 뿐
    - 입력값에서 익은 토마토는 큐에 추가하고, 안 익은 토마토는 개수를 셈.
    - bfs 들어가기 전에, 익은 토마토는 있는데 안 익은 토마토는 없거나, 익은 토마토는 없는데 안 익은 토마토는 있는지 체크.
    - bfs에서 안 익은 토마토를 발견할 때마다 안 익은 토마토 개수에서 1씩 뺀다.
    - bfs 이후, 안 익은 토마토가 남았는제 체크.

## 반례

# Review
- 풀이 시간: 40분
- 처음에는 안 익은 토마토도 큐에 저장하고, bfs 돌린 후에 확인해봄.
    - 그랬더니 너무 메모리가 크고 오래걸림: 136120 KB, 2580 ms
- 그런데 여전히 시간이 오래 걸린다. 어느 부분을 손대야할까?
'''

# Code
# 1. 성공
## 메모리: 48592 KB, 시간: 1828 ms
from collections import deque
import sys
input = sys.stdin.readline

# 열, 행, 높이
m, n, h = map(int, input().split())
# box: 전체 박스, q: 익은 토마토, yet_tomato: 안 익은 토마토
# 1: 익은 토마토, 0: 안 익은 토마토, -1: 빈 칸
box = []
q = deque()
yet_tomato = 0
for z in range(h):
    tmp = []
    for x in range(n):
        row = list(map(int, input().split()))
        tmp.append(row)
        for y in range(m):
            # 익은 토마토를 큐에 담음
            if row[y] == 1:
                q.append((z, x, y))
            # 안 익은 토마토의 개수를 센다.
            elif row[y] == 0:
                yet_tomato += 1
                
    box.append(tmp)
    
# 처음부터 익은 토마토만 있고 안 익은 토마토는 없으면, 0 출력 후 종료
if q and not yet_tomato:
    print(0)
    sys.exit(0)
    
# 처음부터 익은 토마토는 없고 안 익은 토마토만 있으면, -1 출력 후 종료
elif not q and yet_tomato:
    print(-1)
    sys.exit(0)
    
# z, x, y 축
dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

def bfs(q):
    global yet_tomato
    while q:
        z, x, y = q.popleft()
        for a, b, c in zip(dz, dx, dy):
            nz, nx, ny = z + a, x + b, y + c
            # 범위를 벗어날 경우, 지나감
            if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 안 익은 토마토가 있다면, 익음
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append((nz, nx, ny))
                yet_tomato -= 1
                
    return box[z][x][y] - 1

answer = bfs(q)

# 처음에 안 익은 토마토 좌표중에서, 여전히 안 익은 토마토가 존재하는지 확인
if yet_tomato:
    print(-1)
    sys.exit(0)

# 모든 토마토가 익는데 걸리는 최소 일수 출력
print(answer)