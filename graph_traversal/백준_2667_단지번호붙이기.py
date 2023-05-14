n = int(input())
gragh=[]
home=[]

for i in range(n):
    gragh.append(list(map(int, input())))

visit=[[0]*n for _ in range(n)]

#동남서북
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y):
    global cnt
    cnt+=1
    visit[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
            if gragh[nx][ny]==1:
                visit[nx][ny]=1
                dfs(nx,ny)
    return True
    
cnt=0    
result=0
for i in range(n):
    for j in range(n):
        if gragh[i][j]!=0 and visit[i][j]==0:
            if dfs(i,j)==True:
                home.append(cnt)
                result+=1
                cnt=0
home.sort()
print(result)
for i in home:
    print(i)


# 코드 길이 : 912 B
# 시간 : 44 ms
# 메모리 : 31332 KB