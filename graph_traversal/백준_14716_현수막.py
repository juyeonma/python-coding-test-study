'''
# 백준_14716_현수막. 실버 1. 풀이: 23.07.06

# How to
- BFS
- 매번 방문하지 않은 글자 1을 찾아서 연결된 글자 탐색 및 정답 +1
    - 상 하 좌 우 대각선을 살펴서
    - 범위 안이고, 방문하지 않은 글자 1이라면: 큐에 추가, 방문 처리 => 반복
- 한번 bfs를 지나면, 연결된 글자 1은 전부 방문처리(0으로 변환)

# Review
- 전형적인 bfs.
'''

# 성공 Code
from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(x, y):
    # 큐에 추가, 방문 처리
    q = deque([(x, y)])
    arr[x][y] = 0
    
    # 현재 글자와 연결된 글자 전부 탐색
    while q:
        x, y = q.popleft()
        
        # 상 하 좌 우 대각선을 살핀다.
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            
            # 범위 안이고, 방문하지 않은 글자 1이라면: 큐에 추가, 방문 처리
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny]:
                q.append((nx, ny))
                arr[nx][ny] = 0

answer = 0
for x in range(m):
    for y in range(n):
        # 방문하지 않은 글자 1이라면, 연결된 글자 탐색 및 개수 +1
        if arr[x][y]:
            bfs(x, y)
            answer += 1
        
print(answer)
    

'''
# Result
풀이 시간: 15분
메모리: 34176 KB
시간: 156 ms
코드 길이: 1028 B
'''