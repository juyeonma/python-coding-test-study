import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
space = [[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    x,y = map(int,input().split())
    space[x][y]=1

max_trash =0
dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(1,n+1):
    for j in range(1,m+1):
        if not space[i][j]:
            continue
        q = []
        q.append((i,j))
        space[i][j]=0
        area=1
        while q:
            cur_x,cur_y=q.pop()
            for dir in range(4):
                nx,ny = cur_x+dx[dir],cur_y+dy[dir]
                if nx<=0 or ny<=0 or nx>n or ny>m:
                    continue
                if not space[nx][ny]:
                    continue
                q.append((nx,ny))
                space[nx][ny]=0
                area+=1
        if max_trash < area :
            max_trash = area

print(max_trash)

#메모리 31256 시간 56