'''
# 백준_16973_직사각형 탈출. 골드 4. 풀이: 23.07.20 -> 실패 -> 성공

# How to
## 1. pypy 성공
- 격자판은 1, 1 부터 시작
- BFS
- 큐에 시작 좌표를 넣는데, 이때 시작시간 0을 넣어준다.
- 목적지에 도착하면, 소요시간을 return
- 동서남북을 탐색하며 이동
    - 세가지를 체크해야한다:
        - 직사각형이 격자판을 벗어났거나
        - 벽과 겹치거나: 이때, 초반에 벽의 위치를 미리 입력해서 체크해야 시간초과를 방지한다.
        - 이미 방문했는지
    - 이상이 없다면, 이동: 큐에 추가하고, 방문 처리


## 2. 스터디원 풀이 참고하여 python3로 성공
- 직사각형의 좌표:
(x, y)      (x, y+w-1)
(x+h-1, y)  (x+h-1, y+w-1)

- bfs 전에, 먼저 벽과 직사각형이 겹쳐질 좌표를 모두 방문처리
    - 행: i-h+1 ~ i, 열: j-w+1 ~ j 가 겹침
- 사방으로 좌표 이동시에, 먼저 이동 가능한 방향을 구해서 그 곳만 이동했다.
    - 범위 안이고 방문한적 없다면, dir에 추가하여 return 하고, 그 dir로만 이동
        - 이때 1칸씩 이동하므로, 삐져나온 부분만 검사한다. 즉 x 증가라면, 마지막 행만 검사하는 방식.
        - 이렇게 하다보면 아예 사방으로 이동 불가능한 경우, dir이 빈 리스트로 반환된다.
- 좌표 이동시마다 큐에 이동거리를 +1 해서 추가한다.


# Review
- 풀이 시간: 
- 좌표가 1, 1 부터 시작한다는걸 빼먹어서, 계속 실패했다.
- 그런데 좌표 인덱스를 수정한 뒤에도, 계속 시간초과가 났다.
- 결국 원인을 검색하니, 직사각형이 벽과 겹치는지 체크하는게 문제였다.
    - 출처: https://reliablecho-programming.tistory.com/122
    - 벽을 미리 리스트에 저장한 뒤 크기 비교로 체크하니, pypy로 성공했다.
- pypy로도 엄청난 시간이 걸렸는데, 맞힌 사람을 보니까 파이썬으로 적은 시간으로 성공한 사람들이 보인다.
- 더 코드를 효율적으로 바꿀 순 없을까?

- 스터디원 풀이 참고하여 성공하니,
    - 시간이 오래 걸릴 만한 것을 먼저 처리하는게 시간 단축의 키포인트인 것 같다.
    - 즉 먼저 벽과 겹치는 좌표를 모두 방문 처리 후 bfs를 들어가니, 매번 벽을 검사하지 않아도 되어서 6배나 빨라졌다.
    - 미리 이동 가능한 방향을 체크 후 가능한 곳만 이동하는게 더 빠르지만, 일반적인 bfs 처럼 이동 후 체크하는게 훨씬 더 코드가 간결하다.
'''

# Code
# 1. PyPy로 성공
## PyPy3: 메모리: 155628 KB, 시간: 1744 ms
from collections import deque
import sys
input = sys.stdin.readline

# 격자판: n*m
n, m = map(int, input().split())

# 0: 빈 칸, 1: 벽
# 전체 맵과, 벽 리스트: 벽을 별도로 리스트에 저장
paper = []
walls = []
for i in range(n):
    row = list(map(int, input().split()))
    paper.append(row)
    for j in range(m):
        # 0: 빈 칸, 1: 벽
        if row[j] == 1:
            walls.append((i, j))

# 직사각형: h*w, 시작 좌표 (sr, sc), 도착 좌표 (fr, fc)
h, w, sr, sc, fr, fc = map(int, input().split())
sr -= 1
sc -= 1 
fr -= 1
fc -= 1

visited = [[0]*m for _ in range(n)]

# 직사각형이 격자판을 벗어났는거나 벽과 겹쳐졌는지 체크
def check(nx, ny):
    # 격자판을 벗어났는지,
    if nx < 0 or nx+h-1 >= n or ny < 0 or ny+w-1 >= m:
        return True
    
    # 벽은 없는지,
    for wi, wj in walls:
        if nx <= wi < nx+h and ny <= wj < ny+w:
            return True
        
    return False
    
def bfs():
    q = deque([(0, sr, sc)])
    while q:
        t, x, y = q.popleft()
        
        # 목적지에 도착했다면,
        if (x, y) == (fr, fc):
            return t
        
        # 목적지가 아니라면, 방문 처리 후 탐색
        visited[x][y] = 1
        
        for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + i, y + j        
                    
            # 직사각형이 격자판을 벗어났거나 벽과 겹치거나 이미 방문했다면, 넘어감
            if check(nx, ny) or visited[nx][ny]:
                continue

            # 큐에 추가하고, 방문 처리
            q.append((t+1, nx, ny))
            visited[nx][ny] = 1

    return -1

# 만약 도착지점에 직사각형을 댈 수 없다면
# 즉, 도착지점에 직사각형을 놓았을 때 격자판을 벗어나거나 벽과 겹친다면, 실패
if check(fr, fc):
    print(-1)
    sys.exit(0)
    
print(bfs())


# 2. 스터디원 풀이 본 후: python3로 성공
## 메모리: 48156 KB, 시간: 924 ms
'''
- 만약 큐 대신에 paper 좌표로 이동거리를 갱신한다면, 메모리 증가하고 느려짐: 71708 KB, 1064 ms
- 만약 dir을 먼저 구하지 않고 이동 후 해당 방향을 체크한다면, 느려짐: 48284 KB, 1572 ms
- 만약 check 없이 일반적인 bfs처럼 이동 후 체크하면, 조금 느리지만 코드가 훨씬 간편해짐: 48012 KB, 1408 ms
    - if nx < 0 or nx > n-h or ny < 0 or ny > m-w or visited[nx][ny]: continue
'''

from collections import deque
import sys
input = sys.stdin.readline

# 격자판: n*m
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

# 직사각형: h*w, 시작 좌표 (sr, sc), 도착 좌표 (fr, fc)
h, w, sr, sc, fr, fc = map(int, input().split())
sr -= 1
sc -= 1 
fr -= 1
fc -= 1

# 방문 처리
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        # 벽이라면,
        if paper[i][j] == 1:
            # 직사각형과 겹쳐질 좌표를 모두 방문 처리
            # 범위를 벗어나지 않도록 최솟값, 최댓값 사용
            for x in range(max(0, i-h+1), min(n, i+1)):
                for y in range(max(0, j-w+1), min(m, j+1)):
                    visited[x][y] = True

# 격자판을 벗어나지 않고 방문한 적 없는 이동 방향 구하기
def check(x, y):
    dir = []
    # x 증가, y 그대로: 마지막 행(x+h-1)만 +1 해서 검사. 즉, x+h-1 + 1 <= n-1
    if x+h < n and not visited[x+1][y]:
        dir.append((1, 0))

    # x 감소, y 그대로: 첫 행(x)만 -1 해서 검사
    if x-1 >= 0 and not visited[x-1][y]:
        dir.append((-1, 0))

    # x 그대로, y 증가: 마지막 열(y+w-1)만 +1 해서 검사. 즉, y+w-1 + 1 <= m-1
    if y+w < m and not visited[x][y+1]:
        dir.append((0, 1))
        
    # x 그대로, y 감소: 첫 열(y)만 -1 해서 검사
    if y-1 >= 0 and not visited[x][y-1]:
        dir.append((0, -1))

    return dir

def bfs():
    q = deque([(0, sr, sc)])
    while q:
        t, x, y = q.popleft()
        
        # 목적지에 도착했다면,
        if (x, y) == (fr, fc):
            return t
        
        # 목적지가 아니라면, 이동
        for i, j in check(x, y):
            nx, ny = x + i, y + j
                    
            # 큐에 추가하고, 방문 처리
            q.append((t+1, nx, ny))
            visited[nx][ny] = True

    # 목적지에 도달할 수 없다면,
    return -1

visited[sr][sc] = True
print(bfs())