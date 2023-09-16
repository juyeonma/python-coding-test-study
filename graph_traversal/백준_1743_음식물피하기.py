from collections import deque
n,m,k = map(int,input().split())
gragh=[[0]*m for _ in range(n)]
for i in range(k):
    r,c = map(int,input().split())
    gragh[r-1][c-1]=1
    
result=0
dx=[0,0,1,-1]
dy=[-1,1,0,0]
visit=[[0]*m for _ in range(n)]

def bfs(a,b):
    global cnt
    q=deque()
    q.append((a,b))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and gragh[nx][ny]==1 and visit[nx][ny]==0:
                cnt+=1
                visit[nx][ny]=1
                q.append((nx,ny))
    # return cnt

for i in range(n):
    for j in range(m):
        if visit[i][j]==0 and gragh[i][j]==1:
            cnt=0
            bfs(i,j)
            # print(ans)
            result=max(result,cnt)
# print(gragh)
print(result)

#메모리 : 34176 kb
#시간 : 272 ms
#코드길이 : 820 b
#풀이시간 : 33분