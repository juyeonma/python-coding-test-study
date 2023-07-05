import sys
sys.setrecursionlimit(10**6)
m,n,k = map(int,input().split())
rec = [[0]*(n) for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            rec[i][j]=1

dx = [0,0,-1,1]
dy = [-1,1,0,0]    
ans=[]    
res=0
def dfs(x,y):
    global res
    res+=1
    rec[x][y]=1
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<m and 0<=ny<n and rec[nx][ny]==0:
            dfs(nx,ny)
            
cnt=0
for i in range(m):
    for j in range(n):
        if rec[i][j]==0:
            dfs(i,j)
            ans.append(res)
            res=0
            cnt+=1
print(cnt)
ans.sort()
for i in ans:
    print(i,end=' ')

# 시간 : 80 ms
# 메모리 : 32740 KB