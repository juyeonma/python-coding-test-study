# 안전 거리 = 그 칸과 가장 거리가 가까운 아기 사엉와의 거리
# => bfs라고 생각하고 풀었다.

# 못 품 => bfs에 대한 이해도가 아직은 낮은 것 같음..
# visited를 사용해야한다는 고정관념에 사로잡힘8ㅅ8...
# 방향이나 matrix[nx][ny] = matrix[x][y] + 1 같은 개념은 생각해냄!..
# 참고 : https://heytech.tistory.com/137
# 메모리 : 34176KB
# 시간 : 68ms
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(n))
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, 1, 1, -1]
def bfs():
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if matrix[nx][ny] == 0:
                q.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1
q = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append((i, j))
bfs()
# map 함수에 max 함수와 이중 리스트를 입력해 주면,
# 1차원 리스트들 중에서 인덱스 고려없이 최댓값을 포함하는 리스트를 반환
print(max(map(max, matrix))-1)