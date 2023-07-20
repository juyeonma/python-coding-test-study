'''
# 백준_16973_직사각형 탈출. 골드 4. 풀이: 23.07.20 -> 실패 -> 성공

# How to
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



https://reliablecho-programming.tistory.com/122

# Review
- 풀이 시간: 
- 좌표가 1, 1 부터 시작한다는걸 빼먹어서, 계속 실패했다.
- 그런데 좌표 인덱스를 수정한 뒤에도, 계속 시간초과가 났다.
- 결국 원인을 검색하니, 직사각형이 벽과 겹치는지 체크하는게 문제였다.
    - 출처: https://reliablecho-programming.tistory.com/122
    - 벽을 미리 리스트에 저장한 뒤 크기 비교로 체크하니, pypy로 성공했다.
- pypy로도 엄청난 시간이 걸렸는데, 맞힌 사람을 보니까 파이썬으로 적은 시간으로 성공한 사람들이 보인다.
- 더 코드를 효율적으로 바꿀 순 없을까?
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