n = int(input())
city=[list(map(int,input().split())) for _ in range(n)]
d=[[0]*n for _ in range(n)]
dx=[0,1]
dy=[1,0]
max_milk=0
flag=False

def check(i,j):
    global max_milk
    for dir in range(2):
        x=i+dx[dir]
        y=j+dy[dir]
        if x>=n or y>=n:
            continue
        if d[i][j]%3 == city[x][y]:
            d[x][y]=max(d[i][j]+1,d[x][y])
            max_milk=max(d[x][y],max_milk)
        else:
            d[x][y]=max(d[x][y],d[i][j])
        
for i in range(n):
    for j in range(n):
        if city[i][j]==0 and not flag:
            flag=True
            d[i][j]=1
            max_milk=1
        if flag:
          check(i,j)
print(max_milk)
        