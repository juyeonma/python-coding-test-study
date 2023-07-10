# 유닛크기를 같이 이동시키면서 확인하면 되는 문제이다
# 인덱스 오류를 놓쳐서 엄청 헤맸다..


from collections import deque

n,m,a,b,k = map(int,input().split())
board = [[0]*m for _ in range(n)]
vis = [[0]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(k): # 장애물위치 갱신
    x,y=map(int,input().split())
    board[x-1][y-1]=1

s_x,s_y = map(int,input().split()) # 출발위치
s_x-=1
s_y-=1
e_x,e_y = map(int,input().split()) # 도착위치
e_x-=1
e_y-=1

q = deque()
q.append((s_x,s_y))
vis[s_x][s_y]=1
def check(x,y,dir): # 유닛크기를 이동시킬 수있는지 확인
    for i in range(a):
        for j in range(b):
            nx = x+dx[dir]+i
            ny = y+dy[dir]+j
            if nx<0 or ny<0 or nx>=n or ny>=m:
                return False
            if board[nx][ny]==1:
                return False
    return True

while q:
    x,y=q.popleft()
    for dir in range(4):
        nx=x+dx[dir]
        ny=y+dy[dir]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if vis[nx][ny]: # 이미 방문한 위치라면 넘어가기
            continue
        if check(x,y,dir): # 유닛크기를 이동시킬 수 있다면
            vis[nx][ny]=vis[x][y]+1 # 방문처리
            q.append((nx,ny))
if vis[e_x][e_y]:
    print(vis[e_x][e_y]-1)
else:
    print(-1)