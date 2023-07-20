# 전에 풀어봤던 문제인데 일반적인bfs문제에서 z축만 추가해서 풀어주면된다
# 두번째 풀이는 똑같은데 입력값을 sys로 받은것과 사소한 부분을 바꿨더니 400ms정도 감소하였다
from collections import deque

m,n,h = map(int,input().split())
board = [[list(map(int,input().split())) for a in range(n)] for b in range(h)]

dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
dz = [1,-1,0,0,0,0]

zero_count=0 # bfs처리 후 0이 남아있는지 확인하기 위한 변수
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k]==0:
                zero_count+=1 # 0을 모두 카운팅
            if board[i][j][k]==1:
                q.append((i,j,k)) # 처음 익은 토마토 큐에담기

def bfs(zero_count,max_day):
    while q:
        z,x,y=q.popleft()
        for dir in range(6):
            nz = z + dz[dir]
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nz<0 or nz>=h or nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if board[nz][nx][ny]:
                continue
            board[nz][nx][ny]=board[z][x][y]+1
            if max_day<board[nz][nx][ny]: # 모두 익는데까지 걸리는 시간 갱신
                max_day=board[nz][nx][ny]

            zero_count-=1 # 익으면 하나씩 빼기
            q.append((nz,nx,ny))

    if zero_count: # 0이 남아있으면 -1
        return -1
    else: # 0이 없으면 최대값
        return max_day-1

print(bfs(zero_count,1))
#걸린시간 24분
# 메모리 48508kb 시간 2288ms


import sys
from collections import deque

m,n,h = map(int,input().split())
board = [[list(map(int,sys.stdin.readline().split())) for a in range(n)] for b in range(h)]

dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
dz = [1,-1,0,0,0,0]

zero_count=0
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k]==0:
                zero_count+=1
            elif board[i][j][k]==1:
                q.append((i,j,k))

def bfs(zero_count,max_day):
    while q:
        z,x,y=q.popleft()
        for dir in range(6):
            nz = z + dz[dir]
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nz<0 or nz>=h or nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if board[nz][nx][ny]:
                continue
            board[nz][nx][ny]=board[z][x][y]+1
            if max_day<board[nz][nx][ny]:
                max_day=board[nz][nx][ny]

            zero_count-=1
            q.append((nz,nx,ny))

    if zero_count:
        print(-1)
    else:
        print(max_day-1)

bfs(zero_count,1)

#메모리 48464kb 시간 1868ms