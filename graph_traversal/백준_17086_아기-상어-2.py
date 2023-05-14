'''
# 백준_17086_아기 상어 2. 실버 2. 풀이: 23.05.10

# 풀이방법
- 한 점에서 8방향은 모두 1칸 거리이다. 그리고 그 점에서 다시 8방향은 1칸 거리..
- 상어 좌표를 기록해서 bfs 에서 먼저 queue에 넣는다
    - 즉, 상어를 기준으로 둘러싼 8개 좌표의 방문하고, 다시 거기서 8개 좌표를 방문하고..
    - 다만 상어가 1로 표기되기 때문에, 거리에서 1을 빼서 return 해야한다.

# 피드백
- 처음에는 대각선도 거리 계산이 된다길래, 유클리드 거리를 생각했지만, 아니었다.
- 그리고 모든 좌표에서 상어와의 거리를 일일히 구해야 하나 고민했지만, 너무 비효율적이라고 생각했다.
- 그러다가 상어를 둘러싼 좌표는 모두 거리 1이라는걸 생각하고, bfs 코드를 짰다.
- bfs라고 결정하고 나니까 구현은 무척 쉬웠다.
'''

# 풀이 기록
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
shark = []
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        # 상어의 좌표 기록
        if tmp[j] == 1:
            shark.append((i, j))
    
# 대각선을 포함하여 한 지점을 둘러싼 8개의 좌표
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(shark):
    q = deque(shark)
    
    while q:
        x, y = q.popleft()
        # 몇칸 거리인지 측정
        cnt = graph[x][y]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표 범위를 벗어나지 않고, 아직 방문하지 않은 지점이라면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = cnt + 1
        
    # 상어가 1로 표시되어 있으므로, 최종 거리에서 1을 빼서 반환
    return cnt-1

print(bfs(shark))


'''
# 결과
메모리: 34160 KB
시간: 68 ms
코드 길이: 743 B
'''