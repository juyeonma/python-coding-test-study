# 물 수위 조절을 하면서 bfs돌리면 된다
# bfs에서 append처리할 때 실수로 i,j를 넣어서 이 오류를 찾느라 오래걸렸다...

from collections import deque

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check_land(): # 물 수위를 높여가면서 board새로 갱신
    cnt=0
    for i in range(n):
        for j in range(n): 
            if board[i][j]==0:
                cnt+=1
                continue
            board[i][j]-=1
    if cnt==n*n: # 모두 잠겼을 때
        return False
    else: #잠기지 않은 영역이 있을 때
        return True

def bfs():
    vis = [[0]*n for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(n):
            if not vis[i][j] and board[i][j]:
                count+=1
                vis[i][j]=1
                q = deque([(i,j)])
                while q:
                    x,y=q.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if nx<0 or ny<0 or nx>=n or ny>=n:
                            continue
                        if vis[nx][ny] or not board[nx][ny]:
                            continue
                        vis[nx][ny]=1
                        q.append((nx,ny))
    return count

max_count=bfs() # 물 수위 0 
for i in range(1,101): #물 수위 1부터 100까지 확인
    if check_land():
        max_count= max(max_count,bfs())
    else:
        break
print(max_count)

#35분
#메모리 34192kb 시간 752ms