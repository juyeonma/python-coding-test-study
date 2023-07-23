'''
# 백준_2573_빙산. 골드 4. 풀이: 23.07.20 -> 실패 -> 성공

# How to
- BFS 두가지가 필요
    - 1. 1년마다 바다와 접한 빙하가 녹음
    - 2. 매년 빙하의 덩어리 개수를 셈

## 1. 실패
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


## 2. 스터디원 풀이본 후, bfs 2개로: 성공
    - 빙하 녹이기 bfs, 빙하 덩어리 세기 bfs. 총 2개의 bfs 사용
    - 빙하 녹이기
        - 인접한 바다의 개수를 세고, 임시 리스트에 담아 큐가 비었을 때 빙하를 전부 녹인다.
        - 빙하가 남았다면, 기존 큐와 덩어리용 큐에 각각 담는다.
        - 빙하가 녹았다면, 바다가 된다.
    - 빙하 덩어리 세기
        - 빙하 큐를 탐색하며, 각각 빙하마다 연결된 덩어리의 개수를 센다.(bfs)
        - 즉, 반복문이 중첩된다.
        - 하위 큐가 비면(한 덩어리 탐색이 끝나면) 빙하 큐에서 또 좌표를 뽑아서 반복한다.
        - 이때 덩어리가 2개가 되면, 바로 True return
   
   
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

- 스터디원 풀이 본 후 성공:
    - 빙하 덩어리 세는걸 dfs로 했다가 실패했는데, bfs로 하니 성공했다.
'''

# Code
# 1. 실패
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


# 2. 스터디원 풀이본 후, bfs 2개로: 성공
## 메모리: 34480 KB, 시간: 2516 ms
from collections import deque
import sys
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
    check = []
    while q:
        x, y = q.popleft()
        cnt = 0
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            # 테두리는 무조건 바다이므로, 범위 체크는 안해도 된다.
            # 인접한 바다의 개수를 센다.
            if north_pole[nx][ny] == 0:
                cnt += 1
        check.append((x, y, cnt))
        
    cnt_q = deque()
    # 인접한 바다의 개수만큼 빙하가 녹음
    for x, y, cnt in check:
        # 빙하가 남았으면, 기존 큐와 덩어리 카운트용 큐에 각각 담는다.
        if north_pole[x][y] > cnt:
            north_pole[x][y] -= cnt
            q.append((x, y))
            cnt_q.append((x, y))
        # 빙하가 다 녹으면, 바다가 됨
        else:
            north_pole[x][y] = 0
            
    return cnt_q


# 빙하 덩어리 세기
def bfs_cnt(cnt_q):
    visited = [[False] * m for _ in range(n)]
    two = False
    while cnt_q:
        r, c = cnt_q.popleft()
        # 이미 방문했다면, 즉 이전에 덩어리로 셌다면, 넘어감
        if visited[r][c]:
            continue
        
        # 두번째 덩어리라면, return
        if two:
            return True
        
        # 이번에 한 덩어리를 탐색하니, 다음에 두번째 덩어리 때는 return 할 것.
        two = True
        # 이번 덩어리의 큐를 만들고, 덩어리 개수 + 1
        body_q = deque([(r, c)])
        visited[r][c] = True
          
        while body_q:
            x, y = body_q.popleft()
            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j
                # 방문 했거나 바다라면, 넘어감
                if visited[nx][ny] or not north_pole[nx][ny]:
                    continue
                # 방문 처리하고, 큐에 추가
                visited[nx][ny] = True
                body_q.append((nx, ny))
                
    return False


# 1년씩 증가
year = 0
while q:
    year += 1
    # 빙하가 녹고
    cnt_q = bfs_melt(q)
    # 덩어리가 2개라면, year 출력 후 종료
    if bfs_cnt(cnt_q):
        print(year)
        sys.exit(0)
        
# 빙하가 다 녹을 때까지 분리되지 않으면, 0 출력
print(0)