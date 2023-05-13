# 이것도 19분 걸렸다. 순간 아기상어 사이에 거리를 구하는건가 해서 4분만에 이해했다.
# 그 후 쭉 풀었는데 15분동안 풀었다. bfs를돌면서 최솟값으로 나오게하는 부분에서 if문 조건설정에서 좀 오래 걸렸던 것 같다.
# 이렇게 최소값으로 만드는 문제가 많은것같은데 정형화를 할 필요가 있는 것 같다.
# 메모리 34192kb 시간 68ms

from collections import deque

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx=[0,0,1,1,1,-1,-1,-1]
dy=[1,-1,-1,0,1,-1,0,1]

queue =deque()

for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            queue.append((i,j))
def bfs(q):
    while q:
        x,y=q.popleft()
        for x1,y1 in zip(dx,dy):
            nx=x+x1
            ny=y+y1
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if board[nx][ny]==1:
                continue
            if not board[nx][ny]:
                board[nx][ny]=board[x][y]+1
            elif board[nx][ny]>board[x][y]+1:
                board[nx][ny]=board[x][y]+1
            else:
                continue
            q.append((nx,ny))

bfs(queue)
max_distance=0
for i in range(N):
    max_distance=max(max_distance,max(board[i]))

print(max_distance-1)



# 아래처럼 풀면 마지막for문을 안돌면서 최대값을 만들수있고, 안저거리 if문도 더 간략하게 햇다.
# 그런데 시간은 72ms가 걸렸는데 그냥 내부 서버속도차이인것같다. for문이 여러번 겹치지 않고 독립적으로 구성되어 있다면
# 시간복잡도에는 크게 영향을 안준다는 사실을 제대로 알게 되었다.
# 즉 O(n^2) 과 O(n)은 많이 차이나도 O(n)과  O(2n)은 비슷하다는 뜻이다.

# from collections import deque

# N,M = map(int,input().split())
# board = [list(map(int,input().split())) for _ in range(N)]
# dx=[0,0,1,1,1,-1,-1,-1]
# dy=[1,-1,-1,0,1,-1,0,1]

# queue =deque()
# max_distance=0

# for i in range(N):
#     for j in range(M):
#         if board[i][j]==1:
#             queue.append((i,j))
# def bfs(q):
#     global max_distance
#     while q:
#         x,y=q.popleft()
#         for x1,y1 in zip(dx,dy):
#             nx=x+x1
#             ny=y+y1
#             if nx<0 or ny<0 or nx>=N or ny>=M:
#                 continue
#             if board[nx][ny]==1:
#                 continue
#             if board[nx][ny] and board[nx][ny]<=board[x][y]+1: #값이 이미 있는데 들으올 갑이 있으면 queue에 안넣고 탈출
#                 continue
#             else:   # 값이 없거나 들어올값이 더작다면 새롭게 갱신
#                 board[nx][ny]=board[x][y]+1
#                 max_distance=board[nx][ny]
#             q.append((nx,ny))

# bfs(queue)
# print(max_distance-1)


