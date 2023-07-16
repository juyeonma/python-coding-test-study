#이중for문 하나로 bfs돌리고 싶었는데 잘 안돼서 그냥 시간 흐르면서 폭탄 설치와 폭탄 폭발을 나눠서 구했다.

r,c,n = map(int,input().split())
board = [list(map(lambda x:[x,0],input())) for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    for i in range(r): # 1초씩 시간 흐르면서 폭탄설치 시간에 폭탄 설치
        for j in range(c):
            board[i][j][1]+=1
            if board[i][j]==[".",2]:
                board[i][j]=["O",0]

    for i in range(r): # 폭탄 터질 시간에 폭타 폭발시키기
        for j in range(c):
            if board[i][j]==["O",3]:
                board[i][j]=[".",1]
                for dir in range(4):
                    nx = i + dx[dir]
                    ny = j + dy[dir]
                    if nx<0 or ny<0 or nx>=r or ny>=c:
                        continue
                    if board[nx][ny][0]=="O" and board[nx][ny][1]!=3:
                        board[nx][ny]=[".",1]

for k in range(n):
    bfs()

for i in range(r):
    temp = list(map(lambda x:x[0], board[i]))
    print("".join(temp))


#메모리 34324kb 시간 3788ms