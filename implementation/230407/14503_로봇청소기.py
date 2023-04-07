n,m = map(int, input().split())
r,c,d = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
dx = [-1,0,1,0] #북동남서
dy = [0,1,0,-1]

gragh=[[0]*m for _ in range(n)]

x,y=r,c
gragh[x][y]=1

def turn():
    global d
    d-=1
    if d==-1:
        d=3

cnt=1
turn_time=0


while True:
    turn()
    nx=x+dx[d]
    ny=y+dy[d]
    
    if gragh[nx][ny]==0 and arr[nx][ny]==0:
        gragh[nx][ny]=1
        cnt+=1
        x,y=nx,ny
        turn_time=0
        continue
    else:
        turn_time+=1
        
    if turn_time==4:
        nx=x-dx[d]
        ny=y-dy[d]
        if arr[nx][ny]==0:
            x,y=nx,ny
        else:
            break
        turn_time=0
        
print(cnt)
        