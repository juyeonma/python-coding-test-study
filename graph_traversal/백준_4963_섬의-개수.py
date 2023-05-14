'''
# 백준_4963_섬의 개수. 실버 2. 풀이: 23.05.11

# 풀이방법
- 테스트 케이스 갯수가 주어지지 않는데, 어떻게 입력을 받는지 고민했다.
    - 그런데 입력에 '입력의 마지막 줄에는 0이 두 개 주어진다.' 라고 써있었다.

# 보완할 것
- BFS가 DFS 보다 더 빨랐다.
    - BFS는 sys.stdin.readline 여부가 속도에 영향을 미치지 않았다.
- DFS는 RecursionError가 발생하여 sys.setrecursionlimit(10**6)로 최대 재귀 깊이 제한을 풀었다.
'''

# BFS 풀이
from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(x, y):
    q = deque([(x, y)])
    
    while q:
        x, y = q.popleft()
        # 대각선을 포함한 주위 8군데의 섬을 방문
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            # 지도를 벗어나지 않고, 아직 방문하지 않은 섬이라면
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                q.append((nx, ny))
                # 방문 처리
                graph[nx][ny] = 0
                    
while True:
    # 너비, 높이 -> 행=높이, 열=너비
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
    
# DFS 풀이
from collections import deque
import sys
# 최대 재귀 깊이 제한을 늘림
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(x, y):
    # 지도를 벗어나지 않고, 아직 방문하지 않은 섬이라면
    if 0 <= x < h and 0 <= y < w and graph[x][y] == 1:
        # 방문 처리
        graph[x][y] = 0
        # 대각선을 포함한 주위 8군데의 섬을 방문
        for i, j in zip(dx, dy):
            dfs(x+i, y+j)
        return True
    return False

while True:
    # 너비, 높이 -> 행=높이, 열=너비
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)
    

'''
# 결과
## BFS
메모리: 34168 KB
시간: 96 ms
코드 길이: 785 B

## DFS
메모리: 34176 KB
시간: 104 ms
코드 길이: 763 B
'''