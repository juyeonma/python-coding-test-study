# 그냥 평범한 bfs문제였다. 단지 방향에서 대각선이 추가된 정도인 것 같다.
# 시간재면서 풀었는데 그래도 19분정도 걸렸다. 입력값에서 wh가 바뀌어서 한번 실수한점과 함수를 어떻게 뺄지 고민한점 등 때문에 그런 것 같다.
# 또 마음에 걸렸던 점이 변수를 함수안에 선언할때 전역변수에 영향을 끼치게 하려면 global을 써줘야한다. 그래서 vis배열을 사용할때는 사용안해도 되나 라는 생각을 가졌었는데 global없이 가능했다.
# 변수도 global 없이 쓰면 값 변경은 불가능하지만 값 참조는 가능하다.

# 파이썬을 코테용 언어로 사용하는 입장에서 문법적인 부분에 에너지를 쏟는게 맞는건가라는 생각이 들지만, 그래도 해야겠지

# from collections import deque

# dx = [1,1,1,0,0,-1,-1,-1]
# dy = [-1,0,1,-1,1,-1,0,1]

# while True:
#     w,h=map(int,input().split())
#     if w==0 and h==0:
#         break
#     board=[list(map(int,input().split())) for _ in range(h)]
#     vis=[[0]*w for _ in range(h)]
    
#     def bfs(q):
#         while q:
#             x,y=q.popleft()
#             for dir in range(8):
#                 nx=x+dx[dir]
#                 ny=y+dy[dir]
#                 if nx<0 or ny<0 or nx>=h or ny>=w:
#                     continue
#                 if vis[nx][ny] or not board[nx][ny]:
#                     continue
#                 vis[nx][ny]=1
#                 q.append((nx,ny))
#     number_of_island=0

#     for i in range(h):
#         for j in range(w):
#             if vis[i][j] or not board[i][j]:
#                 continue
#             queue=deque([(i,j)])
#             bfs(queue)
#             number_of_island+=1
#     print(number_of_island)
#for dir in range(8):
#   nx=x+dx[dir]
#   ny=y+dy[dir]

#for i,j in zip(dx,dy):
#   nx=x+i
#   ny=y+j

#zip을 이용하면 이렇게도 가능하군요

dx = [1,1,1,0,0,-1,-1,-1]
dy = [-1,0,1,-1,1,-1,0,1]

while True:
    w,h =map(int,input().split())
    if w==0 and h==0:
        break
    square = [list(map(int,input().split())) for _ in range(h)]
    cnt=0

    def dfs(x,y):
        if x<0 or y<0 or x>=h or y>=w:
            return
        if square[x][y]==0:
            return
        square[x][y]=0
        for dir in range(8):
            dfs(x+dx[dir],y+dy[dir])

    for i in range(h):
        for j in range(w):
            if square[i][j]==1:
                dfs(i,j)
                cnt+=1
    print(cnt)