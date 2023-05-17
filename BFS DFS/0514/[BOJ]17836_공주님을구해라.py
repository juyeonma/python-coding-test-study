# 거리니깐 = > bfs
# 칼을 얻어서 거리를 구하는 부분은 구현하지 못함..
# 참고 : https://naa0.tistory.com/236

# 시간 : 68ms
# 메모리 : 34184KB
import sys
from collections import deque
input = sys.stdin.readline
n, m, t = map(int, input().split())
castle = list(list(map(int, input().split())) for _ in range(n))

visited = list([False]*m for _ in range(n))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] 


def bfs():
    global result
    while q:
        x, y, d = q.popleft()

        if x == n-1 and y == m-1:
            result = min(result, d)
            break

        if d+1 > t:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue

            if castle[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny, d+1))
            elif castle[nx][ny] == 1:
                continue
            elif castle[nx][ny] == 2: # 그람 찾음
                temp = d + 1 # 그람까지 온 거리
                temp += abs(n-1 - nx) + abs(m-1 -ny)
                visited[nx][ny] = True

                if temp <= t:
                    result = temp
q = deque()
q.append((0, 0, 0))
visited[0][0] = True
# 양의 무한대
result = float('inf')
bfs()


if t < result:
    print("Fail")
else:
    print(result)