# 메모리 34176kb 시간 64ms
# 걸린시간 : 12분
# 이 문제 또한 전형적인 bfs문제였던 것같다.
# 방문한 곳 표시하면서 bfs돌려서 개수를 세고 리스트에 저장해둔다
# 배열 전체에 대해서 위 방식을 반복한다.
# 마지막에 단지수를 출력하고 단지리스트를 정렬하여 출력한다.

from collections import deque

N = int(input())
square = [list(map(int,input())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dangi = 0
dangi_list = []

vis=[[0]*N for _ in range(N)]

def bfs(q):
    temp=1
    while q:
        x,y=q.popleft()
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if vis[nx][ny] or not square[nx][ny]:
                continue
            temp+=1
            vis[nx][ny]=1
            q.append((nx,ny))
    dangi_list.append(temp)
        

for i in range(N):
    for j in range(N):
        if vis[i][j] or not square[i][j]:
            continue
        vis[i][j]=1
        queue=deque()
        queue.append((i,j))
        bfs(queue)
        dangi+=1

print(dangi)
dangi_list.sort()
for i in dangi_list:
    print(i)