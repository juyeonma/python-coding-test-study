'''
# 백준_2573_빙산. 골드 4. 풀이: 23.07.20 -> 실패

# How to
- BFS 두가지가 필요
    - 1. 1년마다 바다와 접한 빙하가 녹음
    - 2. 매년 빙하의 덩어리 개수를 셈

- 처음에 빙하의 위치를 큐로 저장
- 매번 bfs로 빙하를 녹인다.
    - 인접한 바다의 개수를 세고
    - 빙하가 덜 녹았다면, 새로운 큐에 추가.
    - 빙하가 녹았다면, 임시 큐에 추가 후 한꺼번에 바다로 저장한다.
- dfs로 빙하 덩어리 개수를 센다
    - 현재 북극 상태를 복사해서
    - 현재 빙하의 좌표를 탐색하면서, 덩어리 개수를 센다.
    - dfs 안에서는, 연결된 빙하를 0으로 변환해서 방문처리한다.
    - 덩어리가 2개라면, True, 아니라면 False 반환

## 반례
4 4
0 0 0 0
0 3 1 0
0 1 3 0
0 0 0 0
정답: 1

# Review
- 풀이 시간: 
- 시간 초과 & 메모리 초과.
- 아무래도 매번 북극 상태를 복사하고, 새로운 큐를 만들고 하는 과정에서 메모리가 초과되는 듯 하다.
- 그리고 dfs 부분에서 시간초과까지..
- 빙하 덩어리 개수 세는게 관건인듯 한데, 어떻게 구현해야할까?
'''

# Code
# 1.
## 메모리:  KB, 시간:  ms
from collections import deque
import sys
# 재귀 깊이를 늘려준다.
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

n, m = map(int, input().split())
north_pole = [[0]*m for _ in range(n)]

# 빙하의 위치는 큐에 담기
q = deque()
input()
for x in range(1, n-1):
    row = list(map(int, input().split()))
    north_pole[x] = row
    for y in range(1, m-1):
        if row[y]:
            q.append((x, y))
input()

# 인접한 좌표 탐색
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 빙하 녹이기
def bfs_melt(q):
    new_q = deque()
    melt_q = deque()
    while q:
        x, y = q.popleft()
        cnt = 0
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            # 테두리는 무조건 바다이므로, 범위 체크는 안해도 된다.
            # 인접한 바다의 개수를 센다.
            if north_pole[nx][ny] == 0:
                cnt += 1
                
        # 인접한 바다의 개수만큼 빙하가 녹았을 때, 
        # 여전히 빙하가 남아있다면, 새로운 큐에 추가.
        if north_pole[x][y] - cnt > 0:
            new_q.append((x, y))
            
        # 빙하가 녹았다면, 바다가 될 큐에 추가
        else:
            melt_q.append((x, y))
            
    # 녹은 빙하는 바다가 됨
    for x, y in melt_q:
        north_pole[x][y] = 0
        
    return new_q

# 빙하 덩어리 세기
def dfs_cnt(q):
    # 탐색용 전체 그래프 복사해주기
    north_pole_copy = [i[:] for i in north_pole]
    cnt = 0
    # 한 덩어리씩 재귀로 들어가서, 0으로 변환
    def dfs(x, y):
        if north_pole_copy[x][y]:
            north_pole_copy[x][y] = 0
            dfs_cnt(x+1, y)
            dfs_cnt(x-1, y)
            dfs_cnt(x, y+1)
            dfs_cnt(x, y-1)
        
    # 현재 빙하의 좌표를 탐색하면서, 덩어리 개수 세기
    for x, y in q:
        # 위에 dfs에서 0으로 변환하지 않은, 즉 이미 셈을 한 덩어리가 아니라면
        if north_pole_copy[x][y]:
            dfs(x, y)
            cnt += 1
            
        # 덩어리가 2개라면,
        if cnt == 2:
            return True

    return False

# 1년씩 증가
year = 0
while q:
    year += 1
    # 빙하가 녹고
    q = bfs_melt(q)
    # 덩어리가 2개라면, year 출력 후 종료
    if dfs_cnt(q):
        print(year)
        sys.exit(0)
        
# 빙하가 다 녹을 때까지 분리되지 않으면, 0 출력
print(0)