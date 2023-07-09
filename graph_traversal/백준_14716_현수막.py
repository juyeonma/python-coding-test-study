import sys
sys.setrecursionlimit(3000000)
m,n = map(int,input().split())

gragh=[]
for _ in range(m):
    gragh.append(list(map(int,input().split())))
cnt=0    

def dfs(x,y):
    gragh[x][y]=0
    for k in range(8):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<m and 0<=ny<n and gragh[nx][ny]==1:            
            dfs(nx,ny)

dx=[0,0,-1,1,-1,1,1,-1] #대각선까지 추가되는거를 보지 못해서 헤맸다..
dy=[-1,1,0,0,1,1,-1,-1]
for i in range(m):
    for j in range(n):
        if gragh[i][j]==1:
            dfs(i,j)
            cnt+=1
print(cnt)

# 시간 : 196 ms
# 메모리 : 43668 KB