t = int(input())

def dfs(x,y):
  dx=[0,1,0,-1] #동남서북
  dy=[1,0,-1,0]
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<n and 0<=ny<m:
      if gragh[nx][ny]==1:
        gragh[nx][ny]=-1
        dfs(nx,ny)

for _ in range(t):
  m,n,k = map(int, input().split())
  gragh=[[0]*m for _ in range(n)]
  for i in range(k):
    y,x= map(int, input().split())
    gragh[x][y]=1
  cnt=0
  for i in range(n):
    for j in range(m):
      if gragh[i][j]>0:
        dfs(i,j)
        cnt+=1
  print(cnt)
  
# 코드 길이 : 611 B
# 시간 : 328 ms
# 메모리 : 32676 KB