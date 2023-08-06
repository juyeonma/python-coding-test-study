'''
# 백준_2206_벽 부수고 이동하기. 골드 3. 풀이: 23.07.16 -> 실패

# How to
- 최단 경로
- 벽을 한 개까지 부수고 이동 가능.

## 1. bfs+dfs: 실패
- 평범한 bfs 인데, 벽 부분을 dfs로 구현

## 2. 실패
- 벽 격파 여부를 매번 큐에 넣어서 구분
- 그런데 방문 처리에서 문제가 생김..


## 3. 3차원 visited, bfs: 성공(정답 검색)
- 참고: https://www.acmicpc.net/source/56859392
        https://clap0107.tistory.com/12
- 2번에서 실패한 이유는 벽 제거 상태를 변수에, 이동거리를 큐에 넣었기 때문이었다.
- 이 문제의 포인트는 "3차원 리스트"였다.
    - 큐: 이동거리, x, y, 벽 제거 상태
    - visited: 3중 list. [벽 제거 상태][x좌표][y좌표]

- 다음 칸으로 이동 가능한 경우(범위 안이고, 방문 전일 때)
    - 빈 칸이면: 방문처리, 이동거리 갱신 후 큐에 추가
    - 벽이고, 벽을 제거하기 전이라면: 방문처리, 이동 거리 갱신 및 벽 제거 후 큐에 추가


# Review
- 풀이 시간:
- 시간초과, 메모리초과.
    - 아무래도 방문처리에서 문제가 생긴 것 같다. 
    - 먼저 벽을 부신 경우, 먼저 방문처리가 되어버리면 이후에 더 느리지만 정답인 루트에서 방문된 곳을 방문하지 못해서 문제가 생긴다.

- 스터디 발표를 위해 정답을 찾으면서 3중 리스트가 핵심이라는걸 깨달았다.
- 큐에 원소 3개만 넣고 visited 대신에 board 값 자체를 바꿔도 되긴 하는데, 여튼 핵심은 '3차원'
- 단순히 벽을 1개만 부술 수 있다는 간단한 조건이 추가된 것 뿐인데 난이도가 급 상승한 문제였다..
'''

# Code
# 1. bfs+dfs: 실패
## 메모리:  KB, 시간:  ms
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 0: 빈칸, 1: 벽
arr = [list(input().rstrip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = int(1e9)
def bfs(cnt, x, y, q, check):
    global answer
    
    q.append((cnt, x, y))
    while q:
        # 이동거리 짧은 좌표부터 뽑고, 방문 처리
        cnt, x, y = q.popleft()
        arr[x][y] = '2'
        
        # 동서남북 새로운 좌표 탐색
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            
            # 도착했다면, 이동거리 최솟값 갱신
            if (nx, ny) == (n-1, m-1):
                answer = min(answer, cnt+1)
                return
            
            # 범위 안일 경우
            if 0 <= nx < n and 0 <= ny < m:
                # 빈칸일 경우,
                if arr[nx][ny] == '0':
                    q.append((cnt+1, nx, ny))
                    
                # 벽일 경우,
                elif arr[nx][ny] == '1':
                    # 벽을 부술 수 있다면, 벽 뿌수고 재귀로 들어감.
                    if check and cnt+1 < answer:
                        check = False
                        bfs(cnt+1, nx, ny, q, False)
                        check = True

    return

# 0, 0에서 이동거리 1로 시작
bfs(1, 0, 0, deque(), True)
if answer == int(1e9):
    print(-1)
else:
    print(answer)
    
    
# 2. 실패
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 0: 빈칸, 1: 벽
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    # 0, 0에서 이동거리 1로 시작
    q = deque([(0, 0, 1, True)])
    visited[0][0] = True
    
    while q:
        # 이동거리 짧은 좌표부터 뽑고, 방문 처리
        x, y, cnt, check = q.popleft()
        print(x, y, cnt)
        # 도착했다면, 이동거리 최솟값 갱신
        if (x, y) == (n-1, m-1):
            return cnt
        
        # 동서남북 새로운 좌표 탐색
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j

            # 범위 밖이거나, 이미 방문한 경우:
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue
            
            # 빈칸일 경우
            if arr[nx][ny] == 0:
                q.append((nx, ny, cnt+1, check))
                visited[nx][ny] = True
                
            # 벽인데 뿌실 수 있는 경우,
            elif arr[nx][ny] == 1 and check:
                q.append((nx, ny, cnt+1, False))
                visited[nx][ny] = True

    return -1

print(bfs())


# 3. 3차원 visited, bfs: 성공(정답 검색)
## 메모리: 78448 KB, 시간: 3020 ms
## visited를 [x][y][벽 제거 상태] 순으로 만들면, 메모리와 시간이 증가한다: 151324 KB, 4124 ms
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 0: 빈칸, 1: 벽
board = [list(map(int, input().rstrip())) for _ in range(n)]

# 벽 제거 상태, x좌표, y좌표
visited = [[[0] * m for _ in range(n)] for _ in range(2)]

def bfs():
    # 이동거리, x, y, 벽 제거 상태
    q = deque([(1, 0, 0, 0)])
    # 0, 0 좌표의 벽 제거 전을 방문처리
    visited[0][0][0] = 1
    
    while q:
        cnt, x, y, wall = q.popleft()
        
        # 도착했다면, 이동거리 return
        if (x, y) == (n-1, m-1):
            return cnt
        
        # 동서남북 새로운 좌표 탐색
        for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + i, y + j

            # 범위 밖이거나 방문했다면,
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[wall][nx][ny]:
                continue
            
            # 이동 가능한지 체크
            # 1. 빈 칸이면: 방문처리, 이동거리 갱신 후 큐에 추가
            if not board[nx][ny]:
                visited[wall][nx][ny] = 1
                q.append((cnt+1, nx, ny, wall))
                
            # 2. 벽이고(board[nx][ny]), 벽을 제거하기 전이라면: 방문처리, 이동 거리 갱신 및 벽 제거 후 큐에 추가
            elif not wall:
                visited[1][nx][ny] = 1
                q.append((cnt+1, nx, ny, 1))
                
                
    # 도달할 수 없다면, -1 retrun            
    return -1

print(bfs())