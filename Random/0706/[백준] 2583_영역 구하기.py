# 좌표 설정만 신경쓰면 정석적인 bfs로 풀면된다
# 또 문제를 제대로 안읽고 바로 덤벼들었다.. 그래서 뒤늦게 넓이 구하는걸 넣었다

from collections import deque

m,n,k = map(int,input().split())

board = [[0]*n for _ in range(m)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(k):
    y1,x1,y2,x2 = map(int,input().split())

    for i in range(x1,x2):
        board[i][y1:y2]=[1]*(y2-y1)

def bfs(i,j):
    q = deque([(i,j)])
    size = 1
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x+dx[dir]
            ny = y+dy[dir]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if board[nx][ny]:
                continue
            size+=1
            board[nx][ny]=1
            q.append((nx,ny))
    return size

size_list = []
cnt=0

for i in range(m):
    for j in range(n):
        if board[i][j]==0:
            board[i][j]=1
            size_list.append(bfs(i,j))
            cnt+=1
size_list.sort()
print(cnt)
print(*size_list)

#28분
# 34192kb 시간 76ms