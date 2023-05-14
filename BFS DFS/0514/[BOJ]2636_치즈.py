# 깊어지는 개념이니깐 dfs?!..
# 아이디어가 생각이 나지 않아서 bfs로 풀어보었다. => 이상하게 풀었음 
# => 0이 겉에 있는 1만 변경이 되어야하는데 그러지 못함 => 1에서 0으로 변경해주는 부분을 while문 밖에서 해줘야했다..
# bfs 참고 : https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2636-%EC%B9%98%EC%A6%88-BFS
# => dfs말고 bfs로 푸는 이유 참고 : https://resilient-923.tistory.com/258
# deque()를 이용해 BFS에서 방문했을 때 deque()에 좌표를 넣어주는 과정이 필요하니깐 bfs..!?
# 메모리 : 34176KB
# 시간 : 84ms
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
cnt = 0
for i in range(n):
    matrix.append(list(map(int, input().split())))
    cnt += sum(matrix[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 
# 내 풀이..
# def bfs():
#     global result
#     while q:
#         x, y, d = q.popleft()

#         if x == n-1 and y == m-1:
#             break
#         result = max(result, d)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
#                 continue
            
#             if matrix[nx][ny] == 1:
#                 matrix[nx][ny] = matrix[x][y]+1
#                 visited[nx][ny] = True
#                 q.append((nx, ny, d+1))
#             elif matrix[nx][ny] == 0:
#                 visited[nx][ny] = True
#                 q.append((nx, ny, d))
def bfs():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if matrix[nx][ny] == 0:
                    q.append((nx, ny))
                elif matrix[nx][ny] == 1:
                    melt.append((nx, ny))
    for x, y in melt:
        matrix[x][y] = 0
    return len(melt)
time = 1
while True:
    visited = [[False] * m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0:
        print(time, meltCnt, sep='\n')
        break
    time += 1