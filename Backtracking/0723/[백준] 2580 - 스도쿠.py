처음엔 for문을 통해서 빈칸을 이동했는데 시간이 너무 오래걸릴 것 같아 수정하였다.
하지만 그 후에도 시간초과와의 싸움이 지속됐다
첫 번째 코드는 pypy에서만 돌아가고 두 번째 코드는 python에서도 돌아간다.
두 번째 코드는 질문게시판에서 가로 세로 대각선을 O(1)에 판단 가능하다는 힌트를 얻어 풀었다.
스도쿠 문제에만 몇 시간 투자한 것 같다....

첫 번째 풀이는 모든 경우에서 check_possible_num 함수로 진입하기 때문에 0인 위치가 많아지면 시간이 오래걸린다
반면 두 번째 풀이는 빈칸에서 가능한 숫자의 경우를 이미 배열을 통해 저장해줬기 떄문에 O(1)에 접근이 가능하다


import sys

board = [list(map(int,input().split())) for _ in range(9)]
blank_arr=[]
for i in range(9): #빈칸 찾아서 배열에 넣기
    for j in range(9):
        if board[i][j]==0:
            blank_arr.append((i,j))

def check_possible_num(x,y): # 빈 칸에 들어갈 수 있는 숫자 찾기
    num = {i for i in board[x]}

    for i in range(9):
        num.add(board[i][y])

    r = int(x/3)*3
    w = int(y/3)*3
    for i in range(r,r+3):
        for j in range(w,w+3):
            num.add(board[i][j])

    possible_num={i for i in range(1,10)}
    return possible_num-num

def backtracking(k):
    if k==len(blank_arr): # 모든 빈칸을 채우면 출력하고 종료
        for i in range(9):
            print(*board[i])
        sys.exit()

    x,y=blank_arr[k] 
    possible_num = check_possible_num(x,y) # 빈칸에서 가능한 숫자들 찾기
    
    for i in possible_num: # 가능한 숫자를 차례로 넣어보기
        board[x][y]=i
        backtracking(k+1)
        board[x][y]=0

backtracking(0)



import sys

board = [list(map(int,input().split())) for _ in range(9)]
blank_arr=[] # 빈칸인 위치 
row = [[False]*10 for _ in range(9)] #가로, 세로, 작은 직사각형에서 가능한 숫자 저장을 위한 배열
col = [[False]*10 for _ in range(9)]
rec = [[False]*10 for _ in range(9)]

for i in range(9): #가로 세로 작은 직사각형에서 가능한 숫자들 미리 저장하기
    for j in range(9):
        if board[i][j]:
            row[i][board[i][j]]=True
            col[j][board[i][j]]=True
            rec[(i//3)*3+(j//3)][board[i][j]]=True
        else:
            blank_arr.append((i,j))

def backtracking(k):
    if k==len(blank_arr):
        for i in range(9):
            print(*board[i])
        sys.exit()

    x,y=blank_arr[k]
    for i in range(1,10):
        if not row[x][i] and not col[y][i] and not rec[(x//3)*3+(y//3)][i]: # 숫자들 중에 빈칸에 들어갈 수 있다면
            board[x][y]=i
            row[x][i]=True
            col[y][i]=True
            rec[(x//3)*3+(y//3)][i]=True
            backtracking(k+1)
            row[x][i]=False
            col[y][i]=False
            rec[(x//3)*3+(y//3)][i]=False

backtracking(0)