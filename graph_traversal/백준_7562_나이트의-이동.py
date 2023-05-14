'''
# 백준_7562_나이트의 이동. 실버 1. 풀이: 23.05.10

# 풀이방법
- 나이트는 8군데로 이동할 수 있다.
- BFS
    - 나이트가 한번 이동할 때마다 이동 횟수를 기록하고, 목표지점일 경우 출력
    - 이때, 시작위치를 구별하기 위해서 이동 횟수를 1에서 시작하고, BFS 반환시에 1을 뺀다.

# 보완할 것
- 입력값 자체는 많지 않아서, sys.stdin.readline을 해도 속도 차이가 없다.
- 속도를 빠르게 해보자.
- 시작 위치를 구별하기 위한 더 효율적인 방법은 무엇일까? 여기서는 모든 좌표를 0으로, 시작 좌표를 1로 함으로써 구별하였다.
    - 별도의 queue를 만들어서 이동횟수만 기록하기도 했는데, 속도 차이가 없었다.
'''

# 풀이 기록
from collections import deque

# 나이트가 이동 가능한 위치는 8곳
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(x, y, tx, ty, n, graph):
    q = deque([[x, y]])

    while q:
        x, y = q.popleft()
        cnt = graph[x][y]
        if x == tx and y == ty:
            # 시작위치가 1이었으므로, 1을 빼줘야함
            return cnt-1
        
        # 나이트 이동
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 체스판을 벗어나지 않았고, 아직 가보지 않은 곳이라면
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]==0:
                q.append([nx, ny])
                # 이동 횟수 1번 추가
                graph[nx][ny] = cnt+1

def solve():
    # 체스판: n*n
    n = int(input())
    # x, y 에서 tx, ty로 이동해야함
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())
    
    # 체스판의 이동횟수를 기록
    graph = [[0]*n for _ in range(n)]
    # 시작 위치를 0과 구분을 위해서, 1로 표시
    graph[x][y] = 1

    return bfs(x, y, tx, ty, n, graph)

# 테스트 케이스 만큼 출력
for _ in range(int(input())):
    print(solve())


'''
# 결과
메모리: 34176 KB
시간: 1320 ms
코드 길이: 850 B
'''