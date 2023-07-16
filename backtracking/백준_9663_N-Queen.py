'''
# 백준_9663_N-Queen. 골드 4. 풀이: 23.07.16 -> 실패

# How to
- 체스 퀸 규칙:
    - 일직선으로 앞, 뒤, 옆, 대각선 어떤 방향이든 원하는 만큼 이동할 수 있다.
    - 단 자기 기물은 뚫고 지나갈 수 없다.
    - 상대방 기물을 잡으면 수가 종료.
    
- 퀸이 한번에 갈 수 없는 위치, 8개 중 이후꺼 4개
dx = [1, 1, 2, 2]
dy = [-2, 2, -1, 2]

. X . X .
X . . . X 
. . Q . .
X . . . X
. X . X .

## 반례

# Review
- 풀이 시간:
- 체스 규칙을 몰라서, 찾아봤다.
- 실패: 답이 계속 0이 나온다. 즉 퀸을 n개까지 못 놓는다.
    - 다음 좌표를 어떻게 탐색해야할까?
'''

# Code
# 1. 실패
## 메모리:  KB, 시간:  ms
n = int(input())

dx = [1, 1, 2, 2]
dy = [-2, 2, -1, 2]

answer = 0

def check(x, y):
    # 해당 좌표가 범위 안인지,
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    # 이미 방문한건 아닌지
    if chess[x][y]:
        return False
    
    # 행
    for ii in range(n):
        if chess[x][ii]:
            return False

    # 열
    for ii in range(n):
        if chess[ii][y]:
            return False
        
    # 대각선
    for ix, iy in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
        for ii in range(1, n):
            nx, ny = x+ii*ix, y+ii*iy
            if 0 <= nx < n and 0 <= ny < n and chess[nx][ny]:
                return False
            
    return True
            
def dfs(x, y, cnt):
    global answer
    
    # 퀸을 n개 다 높은 경우, 경우의 수 +1
    if cnt == n:
        answer += 1
        return
    
    for i, j in zip(dx, dy):
        nx, ny = x + i, y + j
        # 높아도 된다면,
        if check(nx, ny):
            chess[nx][ny] = True
            dfs(nx, ny, cnt+1)
            chess[nx][ny] = False

# 모든 좌표 탐색
for x in range(n):
    for y in range(n):
        chess = [[False] * n for _ in range(n)]
        dfs(x, y, 0)
    
print(answer)