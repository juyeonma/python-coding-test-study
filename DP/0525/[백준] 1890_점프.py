# 전에 풀어본 문제인데 풀지 못했다..
# bfs로 풀리는 것 같아서 했는데 자꾸 틀렸다.
# bfs로도 풀 수 있을 것 같긴 한데 조건을 잘 설정해줘야될 것 같다. 아닌가?
# dp로는 무조건 n^2안에 끝나기 때문에 안전하게 풀 수 있다.
# dp인 것을 모르고 본다면 dp로 풀 생각을 전혀 하지 못했을 것 같은데... 경험을 많이 해보자
# from collections import deque

# n= int(input())
# board=[list(map(int,input().split())) for _ in range(n)]
# d = [[0]*n for _ in range(n)]

# dx = [0,1]
# dy = [1,0]

# q= deque([(0,0)])
# while q:
#     x,y=q.popleft()
#     for dir in range(2):
#         nx = x + dx[dir]*board[x][y]
#         ny = y + dy[dir]*board[x][y]
#         if nx<0 or ny<0 or nx>=n or ny>=n:
#             continue
#         if nx==n-1 and ny==n-1:
#             d[nx][ny]+=1
#             continue
#         if d[nx][ny]:
#             continue
#         d[nx][ny]=1
#         q.append((nx,ny))
# print(d[-1][-1])

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0]=1
for i in range(n):
    for j in range(n):
        if not d[i][j]:
            continue
        if i==n-1 and j==n-1: #여기서의 값은 0이기때문에 break를 하지 않으면 중복으로 더해진다. 그렇기때문에 마지막 위치에 도달하면 탈출
            break
        if i+board[i][j]<n:
            d[i+board[i][j]][j]+=d[i][j]
        if j+board[i][j]<n:
            d[i][j+board[i][j]]+=d[i][j]
print(d[-1][-1])