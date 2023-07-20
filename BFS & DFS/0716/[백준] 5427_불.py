# 생각보다 복잡해서 오래 걸렸다. 아래 풀이가 더 bfs스럽게 푼 것 같다
# 불과 상근이를 하나의 큐로 구해보고 싶은데...

from collections import deque

n = int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def check_st_pos_fire_pos(arr,vis):  # 상근이와 불의 처음 위치 구하기
    w,h = len(arr[0]),len(arr)
    fire_pos = deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j]=="@":
                st_pos = deque([(i,j)])
                vis[i][j]=1
            if arr[i][j]=="*":
                fire_pos.append((i,j))
                vis[i][j]="fire"

    return st_pos,fire_pos

def move_fire(fire_pos,building,vis): # 불 한칸 이동시키기
    length = len(fire_pos)
    for _ in range(length):
        x,y=fire_pos.popleft()
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if nx<0 or ny<0 or nx>=len(vis) or ny>=len(vis[0]):
                continue
            if vis[nx][ny]=="fire" or building[nx][ny]=="#":
                continue
            vis[nx][ny]="fire"
            fire_pos.append((nx,ny))
            
def move_sang(sang_pos,building,vis): # 상근이 한칸 이동시키기
    length = len(sang_pos)
    for _ in range(length):
        x,y=sang_pos.popleft()
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if nx<0 or ny<0 or nx>=len(vis) or ny>=len(vis[0]): # 탈출했다면
                return "LIVE"
            if vis[nx][ny]=="fire" or vis[nx][ny]==1 or building[nx][ny]=="#":
                continue
            vis[nx][ny]=1
            sang_pos.append((nx,ny))

    if len(sang_pos): # 가는게 가능하면 
        return "POSSIBLE"
    else: # 갈 곳이 없으면
        return "IMPOSSIBLE"
            
def testcase():
    w,h = map(int,input().split())
    building = [list(input()) for _ in range(h)]
    vis = [[0]*w for _ in range(h)]
    sang_pos,fire_pos = check_st_pos_fire_pos(building,vis)
    cnt=1
    while True:
        move_fire(fire_pos,building,vis) # 불먼저 옮기기
        status = move_sang(sang_pos,building,vis) # 상근이 이동
        if status=="POSSIBLE": # 상근이 이동 가능이면 카운팅
            cnt+=1
        elif status=="IMPOSSIBLE": #상근이 이동 불가능이면 불가능문구 출력
            return status
        else: # 살아남았다면 걸린시간 출력
            return cnt

for _ in range(n):
    print(testcase())

#걸린시간 1시간 1분
# 메모리 57060kb 시간 2676ms



from collections import deque
    
def move_fire(building,vis,w,h):
    fire_pos = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j]=="*":
                fire_pos.append((i,j))
                vis[i][j]=1

    while fire_pos:
        x,y = fire_pos.popleft()
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if nx<0 or ny<0 or nx>=h or ny>=w:
                continue
            if vis[nx][ny] or building[nx][ny]=="#":
                continue
            vis[nx][ny]=vis[x][y]+1
            fire_pos.append((nx,ny))

def move_sang(building,vis,w,h):
    sang_pos = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j]=="@":
                sang_pos.append((i,j))
                vis[i][j]=1
    while sang_pos:
        x,y = sang_pos.popleft()
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if nx<0 or ny<0 or nx>=h or ny>=w:
                return vis[x][y]
            if building[nx][ny]=="#" or (vis[nx][ny] and vis[nx][ny]<=vis[x][y]+1):
                continue
            vis[nx][ny]=vis[x][y]+1
            sang_pos.append((nx,ny))
    
    return "IMPOSSIBLE"

def testcase():
    w,h = map(int,input().split())
    building = [list(input()) for _ in range(h)]
    vis = [[0]*w for _ in range(h)]
    move_fire(building,vis,w,h)
    print(move_sang(building,vis,w,h))

n = int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(n):
    testcase()

#메모리 77100 시간 2252ms