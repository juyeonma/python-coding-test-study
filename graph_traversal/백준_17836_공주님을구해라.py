from collections import deque

n, m, t = map(int, input().split())
gragh=[]
for _ in range(n):
    gragh.append(list(map(int, input().split())))

visit=[[0]*m for _ in range(n)]

def bfs(xx,yy):
    dx=[0,0,1,-1]
    dy=[-1,1,0,0]
    ans=10001
    q=deque()
    q.append((xx,yy))
    visit[xx][yy]=1
    while q:
        x,y=q.popleft()
        if gragh[x][y]==2: #검을 주웠다면 목표 지점까지 걸리는 가장 짧은 거리를 구함
            ans=abs(n-1-x)+abs(m-1-y)+visit[x][y]-1 #가로로 남은 거리 + 세로로 남은거리+지금까지 온 거리
        
        if (x,y)==(n-1,m-1): #검이 없다면
            return min(visit[x][y]-1, ans) #가장 작은 값
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and gragh[nx][ny]!=1 :
                if visit[nx][ny]==0:
                    visit[nx][ny]=visit[x][y]+1
                    q.append((nx,ny))
    return ans
res=bfs(0,0) #res에 따로 선언해줘야함
if res<=t:
    print(res)
else:
    print("Fail")
    
    
# 코드 길이 : 838 B
# 시간 : 76 ms
# 메모리 : 34192 KB