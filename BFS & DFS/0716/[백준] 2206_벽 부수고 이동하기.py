
첫번째 코드는 백트래킹으로 해봤는데 역시 시간초과였다.
백트래킹 써본 것에 만족하자

맵을 한번만 돌면서 풀어야 되는 것 같은데 잘몰라서 답을봤다
간만에 3중for문이었다. 게다가 약간 재귀의 특징이 들어있는 듯한 느낌이다.
그래서 쉽게 생각할 수 없었던 것 같다
골드 3은 처음 풀어보는 데 완전 다른 유형의 bfs였다...

시간초과 코드
# import sys
# sys.setrecursionlimit(10**6)

# n,m = map(int,input().split())
# board = [list(input()) for _ in range(n)]
# vis = [[0]*m for _ in range(n)]

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# answer = 1000001
# def func(x,y,k):
#     global answer

#     if x==n-1 and y==m-1:
#         answer = min(answer,vis[x][y])

#     for dir in range(4):
#         nx=x+dx[dir]
#         ny=y+dy[dir]
#         if nx<0 or ny<0 or nx>=n or ny>=m:
#             continue
#         if vis[nx][ny]:
#             continue
#         vis[nx][ny] = vis[x][y] + 1
#         if board[nx][ny] == "0":
#             func(nx,ny,k)
#         if board[nx][ny] == "1" and k==0:
#             func(nx,ny,1)
#         vis[nx][ny]=0
# vis[0][0]=1
# func(0,0,0)
# if answer==1000001:
#     print(-1)
# else:
#     print(answer)

from collections import deque
n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
vis = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque([(0,0,0)])
    vis[0][0][0]=1
    while q:
        x,y,wall=q.popleft() # wall은 벽을 한번 뚫었는지 확인하기 위한 용도

        if x ==n-1 and y==m-1: # bfs이므로 가장 먼저 도달한 값을 리턴
            return vis[x][y][wall]

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if vis[nx][ny][wall]:
                continue
            if board[nx][ny]=="0":
                q.append((nx,ny,wall))
                vis[nx][ny][wall]= vis[x][y][wall]+1

            if board[nx][ny]=="1" and wall==0:
                q.append((nx,ny,1))
                vis[nx][ny][1] = vis[x][y][wall]+1

    return -1

print(bfs())