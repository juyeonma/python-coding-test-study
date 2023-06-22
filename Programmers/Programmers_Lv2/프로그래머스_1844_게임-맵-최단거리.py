'''
# 프로그래머스_1844_게임 맵 최단거리. Lv 2. 풀이: 23.06.22

# How to
- deque 사용: x, y, d(거리)
- 0, 0, 1부터 시작
- 매번 동서남북을 돌면서 범위 안이고, 길이고, 방문하지 않았는지 확인한다.   
    - 만약 상대팀에 도착했다면, d+1을 return
    - 아직 도착하지 않았다면, nx, ny, d+1을 큐에 넣고 방문처리.
- 큐가 빌 때까지 도착하지 않았다면, 도착할 수 없는 것이므로 -1 return    

# Review
- 전형적인 BFS 였다.
'''

# Code
from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    # 도착지점
    ex, ey = n-1, m-1
    visited = [[False] * m for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    # 0, 0 좌표, 거리 1부터 시작
    q = deque([(0, 0, 1)])
    while q:
        x, y, d = q.popleft()
        for i, j in zip(dx, dy):
            nx = x+i
            ny = y+j
            # 범위 안이고, 길이고, 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and not visited[nx][ny]:
                # 만약 상대팀에 도착했다면, 거리 return
                if (nx, ny) == (ex, ey):
                    return d+1
                # 아직 도착하지 않았다면, 큐에 넣고 방문처리
                q.append((nx, ny, d+1))
                visited[nx][ny] = True
                
    # 도착할 수 없으므로,
    return -1

'''
# Result
풀이 시간: 15분
효율성 테스트 1 〉통과 (12.66ms, 10.4MB)
'''