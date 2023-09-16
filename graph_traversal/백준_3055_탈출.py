# 다시 풀기..(이해는 되지만 구현을 못하겠다)
from collections import deque

r,c = map(int,input().split())
gragh=[]
for i in range(r):
    gragh.append(list(input()))
    
dx=[0,0,-1,1]
dy=[1,-1,0,0]

visit=[[0]*c for _ in range(r)]

q=deque()

def bfs(a,b):
    q.append((a,b))
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if (gragh[nx][ny]=="." or gragh[nx][ny]=="D") and gragh[x][y]=="S":
                    gragh[nx][ny]="S"
                    visit[nx][ny]=visit[x][y]+1
                    q.append((nx,ny))
                elif (gragh[nx][ny]=="." or gragh[nx][ny]=="S") and gragh[x][y]=="*":
                    gragh[nx][ny]="*"
                    q.append((nx,ny))
    return "KAKTUS"
    
