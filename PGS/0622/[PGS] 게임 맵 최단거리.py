#  전형적인 bfs 문제였다. 방문처리를 하면서 bfs돌리면 된다

from collections import deque

def solution(maps):
    w = len(maps[0])
    h = len(maps)
    
    vis = [[0]*w for _ in range(h)]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = deque()
    q.append([0,0])
    vis[0][0]=1
    while q:
        x,y=q.popleft()
        for dir in range(4):
            nx = x+dx[dir]
            ny = y+dy[dir]
            if nx<0 or ny<0 or nx>= h or ny >= w:
                continue
            if maps[nx][ny]==0 or vis[nx][ny]:
                continue
            vis[nx][ny]=vis[x][y]+1
            q.append([nx,ny])
            if nx==h-1 and ny==w-1:
                return vis[nx][ny]
    if vis[-1][-1]==0:
        return -1
    
# 시간 못쟀는데.. 10분?