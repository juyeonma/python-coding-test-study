# 백트래킹의 느낌이 났는데 백트래킹 하는 법을 몰라서 다른 방식으로 풀었습니다.
# 백트래킹 공부하기!

from itertools import combinations

N =int(input())
flowers = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
memo = []

for i in range(N):
    for j in range(N):
        memo.append([i,j])

c= combinations(memo,3)
cost = 20000
for positions in c:
    vis=[[0 for _ in range(N)] for _ in range(N)]
    temp_cost=0
    flag=False
    for position in positions:
        x,y=position
        if vis[x][y]:
            break
        vis[x][y]=1
        temp_cost+=flowers[x][y]
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                flag=True
                break
            if vis[nx][ny]:
                flag=True
                break
            vis[nx][ny]=1
            temp_cost+=flowers[nx][ny]
        if flag:
            break
    else:
        cost = min(temp_cost,cost)
print(cost)