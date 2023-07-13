'''
# 백준_2468_안전 영역. 실버 1. 풀이: 23.07.10

# How to
- BFS
- 비의 양은 0에서 시작해서, 영역의 최고 높이까지 탐색하면서 안전 영역의 최대 개수 갱신
    - 비의 양보다 높고 방문 전이라면: bfs로 탐색, 안전영역 개수 +1
    - 높이가 낮다면: 물에 잠기고, 방문 처리
    - 높다면: 큐에 추가, 방문 처리
    
- 매번 안전 영역의 개수와 방문 리스트를 초기화

## 반례
"아무 지역도 물에 잠기지 않을 수도 있다."

# Review
- 풀이 시간: 30분
- 속도가 빠르지 않다.. 맞힌 사람 코드를 보니, 대체로 bfs가 아니라 다른 로직으로 푼 듯 하다.
'''

# Code
# 1. 성공
## 메모리: 34192 KB, 시간: 948 ms
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]

# 가장 높은 좌표
max_rain = max(map(lambda x: max(x), city))

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        # 사방을 살피며 연결된 좌표 탐색
        for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx = x + i
            ny = y + j
            
            # 범위를 벗어났다면, 지나감
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            # 높이가 낮다면: 물에 잠기고, 방문 처리
            if city[nx][ny] <= rain:
                city[nx][ny] = 0
                visited[nx][ny] = True
                
            # 비의 양보다 높고, 방문 전이라면: 큐에 추가, 방문 처리
            elif not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                
answer = 0
for rain in range(max_rain+1):
    # 매번 안전 영역의 개수와 방문 리스트를 초기화
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # 비의 양보다 높고 방문 전이라면: bfs로 탐색, 안전영역 개수 +1
            if city[x][y] > rain and not visited[x][y]:
                bfs(x, y)
                cnt += 1
    
    # 안전 영역의 최대 개수 갱신
    answer = max(answer, cnt)

print(answer)


# 2. 만약 영역별 높이의 집합을 구한다면,
## 34176 KB 960 ms
'''
city = []
city_height = set()
for _ in range(n):
    tmp = list(map(int, input().split()))
    city.append(tmp)
    city_height.update(tmp)

# 비가 안 올수도 있으므로, 0 추가
for rain in [0]+sorted(city_height):
    pass
'''