# 각 땅마다 인접한 부분들을 bfs처럼 확인하고 각 구역을 기억해둔다
# 기억해둔 곳을 돌면서 지도를 새롭게 갱신한다
# 한 줄이 바다로 이루어져 있으면 다음 줄을 확인하는 방식으로
# 왼쪽 오른쪽 위쪽 아래쪽 모두 확인해본다
# 한줄이 바다로 이루어져있는지를 확인하는 것을 좀 더 잘 짜고 싶어서 고민하다가
# 그냥 아래코드처럼 해버렸다.

r,c = map(int,input().split())
board = [list(input()) for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

byeland = []
for i in range(r):
    for j in range(c):
        if board[i][j]=="X":
            cnt=0
            for dir in range(4):
                nx=i+dx[dir]
                ny=j+dy[dir]
                if nx<0 or ny<0 or nx>=r or ny>=c:
                    cnt+=1
                    continue
                if board[nx][ny]==".":
                    cnt+=1
                    continue
                
            if cnt>=3:
                byeland.append((i,j))

for x,y in byeland:
    board[x][y]="."

top=0
bottom=r-1
left=0
right=c-1

for i in range(r):
    top=i
    flag=True
    for j in range(c):
        if board[i][j]=="X":
            flag=False
            break
    if not flag:
        break

for i in range(r-1,-1,-1):
    bottom=i
    flag=True
    for j in range(c):
        if board[i][j]=="X":
            flag=False
            break
    if not flag:
        break

for i in range(c):
    left=i
    flag=True
    for j in range(r):
        if board[j][i]=="X":
            flag=False
            break
    if not flag:
        break

for i in range(c-1,-1,-1):
    right=i
    flag=True
    for j in range(r):
        if board[j][i]=="X":
            flag=False
            break
    if not flag:
        break

for i in range(top,bottom+1):
    print("".join(board[i][left:right+1]))

#38분




r,c = map(int,input().split())
board = [list(input()) for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

byeland = []
top=r-1
bottom=0
left=c-1
right=0

for i in range(r):
    for j in range(c):
        if board[i][j]=="X":
            cnt=0
            for dir in range(4):
                nx=i+dx[dir]
                ny=j+dy[dir]
                if nx<0 or ny<0 or nx>=r or ny>=c:
                    cnt+=1
                    continue
                if board[nx][ny]==".":
                    cnt+=1
                    continue
                
            if cnt>=3:
                byeland.append((i,j))
            else:
                top = min(top,i)
                bottom = max(bottom,i)
                left = min(left,j)
                right = max(right,j)
                

for x,y in byeland:
    board[x][y]="."

for i in range(top,bottom+1):
    print("".join(board[i][left:right+1]))