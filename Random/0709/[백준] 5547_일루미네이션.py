# 흰색 위치를 이용해서 구해야되나 싶긴했는데 그 이후로 생각이 잘안됐다.
# 알고보니 가상의 테두리를 만들어서 bfs를 돌리면 되는 문제였다.
# 이 아이디어만 생각할 수 있다면 어렵지는 않은 문제같지만, 이 아이디어가 핵심인 듯 하다
# 또한 x와 y가 바뀌어 있어서 헤갈렸다.

# 홀수줄과 짝수줄에서 이동할 수 있는 위치가 다르므로 구분해서 풀어야한다.

from collections import deque

w,h = map(int,input().split())
board = [[0]*(w+2) for _ in range(h+2)]
vis = [[0]*(w+2) for _ in range(h+2)]

for i in range(1,h+1):
    board[i][1:w+1] = map(int,input().split())

dx=[-1,-1,0,1,1,0]
dy=[[-1,0,1,0,-1,-1],[0,1,1,1,0,-1,-1]]

q = deque([(0,0)])
vis[0][0]=1
count=0
while q:
    x,y=q.popleft()
    for dir in range(6):
        nx = x + dx[dir]
        ny = y + dy[x%2][dir] # 짝수줄과 홀수줄 구분
        if nx<0 or ny<0 or nx>=h+2 or ny>=w+2:
            continue
        if board[nx][ny]==1:
            count+=1
        elif board[nx][ny]==0 and vis[nx][ny]==0:
            vis[nx][ny]=1
            q.append((nx,ny))

print(count)