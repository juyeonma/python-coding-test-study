# 유형 : 최단거리 => bfs

# 실패
# 채점 결과
# 정확성: 25.6
# 효율성: 22.6
# 합계: 48.1 / 100.0
# 문제점 => if nx >= n부분에서 n과 m을 바꿔서 잘못 적었다..
# 고치니 통과!
from collections import deque
def bfs(q, n, m, visited, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny < 0 or ny >= m or visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            maps[nx][ny] = maps[x][y] + 1
            q.append((nx, ny))

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                visited[i][j] = True
    q = deque([(0, 0)])
    visited[0][0] = True
    bfs(q, n, m, visited, maps)

    answer = -1
    if maps[n-1][m-1] > 1:
        answer = maps[n-1][m-1]
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])

# 속도
# 효율성  테스트
# 테스트 1 〉	통과 (12.53ms, 10.3MB)
# 테스트 2 〉	통과 (3.74ms, 10.3MB)

# 정석 bfs라서 그나마 빠르게 풀 수 있었던 것 같다..