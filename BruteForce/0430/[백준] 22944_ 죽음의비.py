# bfs문제는 나름 좀 자신 있었는데 67% 부근에서 자꾸 틀렸다.
# 자꾸 틀리니까 멘탈이 나가서 스스로의 논리 지옥에 빠진 것 같다.
# 항상 전략을 짜고 문제를 풀기로 마음먹었는데 이 문제는 그냥 대충만 짜놓고 바로 문제를 풀어서 그런 것 같다.

# 함수를 활용해서 문제를 푸는 연습을 하는것도 좋을 것 같다. flag로 탈출 하는 것보다 함수를 쓰면 return으로 나갈 수 있기 때문에 더 깔끔한 풀이를 할 수 있을 것 같다.

# bfs를 풀때 queue에 넣는 건 항상 좌표만 넣어왔어서 이 문제처럼 다른 요소까지 넣는다는 생각을 못했다. 고정관념이 생긴 듯 하다.
# 좀더 유연한 사고를 해야겠다

# 틀린이유가 다음에 가야할 위치에서 해당 칸보다 체력이 높은지를 비교하는 것을 사용하지않아서 자꾸 틀린것같다.
# 이 작업을 안하고 한번 방문한 곳은 방문하지 못하게 해서 체력이 높게 갱신이 안돼서 틀린 것 같다.

from collections import deque

N,H,D = map(int,input().split())
board = [list(input()) for _ in range(N)]
vis = [[0]*N for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
queue = deque()
for i in range(N):
    for j in range(N):
        if board[i][j]=="S":
            queue.append((i,j,H,0,0))
            vis[i][j]=H
flag =False
while queue:
    x,y,now_h,now_d,cnt=queue.popleft()
    
    for dir in range(4):
        nx = x+dx[dir]
        ny = y+dy[dir]

        if nx<0 or ny<0 or nx>=N or ny>=N:
            continue
        if board[nx][ny]=="E":
            print(cnt+1)
            flag=True
            break
        nxt_h = now_h
        nxt_d = now_d

        if board[nx][ny]=="U":
            nxt_d = D
        if nxt_d == 0:
            nxt_h -= 1
        else:
            nxt_d -= 1

        if nxt_h == 0:
            continue
        if vis[nx][ny] < nxt_h:
            vis[nx][ny]= nxt_h
            queue.append((nx,ny,nxt_h,nxt_d,cnt+1))
    if flag:
        break
else:
    print(-1)