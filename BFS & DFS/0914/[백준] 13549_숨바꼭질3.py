from collections import deque
import sys
input = sys.stdin.readline

a,b = list(map(int,input().split()))
q =deque()
q.append(a)
vis = [-1 for _ in range(100001)]
vis[a]=0

while q:
    x= q.popleft()
    if x==b:
        print(vis[b])
        break
    # for dx in [x-1,x+1]:
    #     if 0<=dx<=100000 and vis[dx]==-1:
    #         vis[dx]=vis[x]+1
    #         q.append(dx)
    if 0<=x-1<=100000 and vis[x-1]==-1:
        vis[x-1]=vis[x]+1
        q.append(x-1)
    if 0<=2*x<=100000 and vis[2*x]==-1:
        vis[2*x]=vis[x]
        q.appendleft(2*x)
    if 0<=x+1<=100000 and vis[x+1]==-1:
        vis[x+1]=vis[x]+1
        q.append(x+1)





# vis =[[False,0] for _ in range(100001)]
# vis[a] = [True,0]
# def bfs():
#     q = deque()
#     q.append(a)
#     while q:
#         x=q.popleft()
#         dx = [x+1,x-1,2*x]
#         for dir in range(3):
#             nx=dx[dir]
#             if nx<0 or nx>100000:
#                 continue
#             if dir==2:
#                 if vis[nx][0]==True:
#                     if vis[nx][1]>vis[x][1]:
#                         vis[nx][1]=vis[x][1]
#                         q.append(nx)
#                 else:
#                     vis[nx][0]=True
#                     vis[nx][1]=vis[x][1]
#                     q.append(nx)
#             else:
#                 if vis[nx][0]==False:
#                     vis[nx][1]=vis[x][1]+1
#                     vis[nx][0]=True
#                     q.append(nx)
#     print(vis[b][1])
#     return
# if a==b:
#     print(0)
# else:
#     bfs()
