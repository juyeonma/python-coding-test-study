첫번째 풀이는 시간초과로 통과가 안된다
2중 배열을 만들어서 안되는 줄을 갱신하는 방식으로 해서 시간이 많이 걸렸다

두번째 풀이도 시간초과였다 첫번째보다는 시간이 많이 줄었지만 
기본 3중 for문에 조건도 많아서 아직 시간초과가 나는 것 같다

세번째 풀이는 두번째 풀이를 수정한 풀이인데 첫번째 두번째보다는 엄청 빠르긴하지만 시간초과를 피할 수 없었다.

네번째 풀이는 세로와 대각선의 같은 선에 있는 부분을 배열 방문처리로 풀었다.
각 부분을 배열 인덱스로 확인하기 때문에 O(1)에 확인이 가능하고 한 함수에 for문이 하나라서 통과되었다.


시간초과
첫번째 풀이
import sys
sys.setrecursionlimit(10**6)

n = int(input())
board = [[0]*n for _ in range(n)]
count=0

dx = [1,1,1,0,0,-1,-1,-1]
dy = [0,1,-1,1,-1,1,0,-1]

def is_possible_attack(i,j):
    for dir in range(8):
        nx=i
        ny=j
        while True:
            nx += dx[dir]
            ny += dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                break
            if board[nx][ny]==1:
                return True
    return False

def func(m_x,m_y,k):
    global count
    
    if m_y==n:
        m_y=0
        m_x+=1
    
    if k==n:
        count+=1
        return

    for i in range(m_x,n):
        for j in range(m_y,n):
            if not board[i][j]:
                board[i][j]=1
                if is_possible_attack(i,j):
                    board[i][j]=0
                    continue
                func(m_x,m_y+1,k+1)
                board[i][j]=0

func(0,0,0)
print(count)


두번째 풀이 -시간초과
import sys
sys.setrecursionlimit(10**6)

n = int(input())
count=0
vis = set()

def is_possible_attack(i,j):
    for x,y in vis:
        a=x-i
        b=y-j
        if a==0 or b==0 or (abs(a) == abs(b)):
            return True
    
    return False
        
def func(m_x,m_y):
    global count
    
    if m_y==n:
        m_y=0
        m_x+=1
    
    if len(vis)==n:
        count+=1
        return

    for i in range(m_x,n):
        for j in range(m_y,n):
            if (i,j) not in vis:
                 if not is_possible_attack(i,j):
                    vis.add((i,j))
                    func(m_x,m_y+1)
                    vis.remove((i,j))
            else:
                continue

func(0,0)
print(count)



세번째 풀이 - 시간 초과
n = int(input())
count=0
vis = set()

def is_possible_attack(i,j):
    for x,y in vis:
        a=x-i
        b=y-j
        if a==0 or b==0 or (abs(a) == abs(b)):
            return True
    
    return False
        
def func(x):
    global count
    
    if x==n:
        count+=1
        return
    
    for y in range(n):
        if not is_possible_attack(x,y):
            vis.add((x,y))
            func(x+1)
            vis.remove((x,y))

func(0)
print(count)


네번째풀이 - 통과풀이
n = int(input())
isused1 = [False]*n  # 같은 열인지 확인하는 배열
isused2 = [False]*((2*n)-1) # 오른쪽 아래로 가는 대각선으로 같은지 확인하는 배열
isused3 = [False]*((2*n)-1) # 왼쪽 아래로 가는 대각선으로 같은지 확인하는 배열
res=0 # 경우의수

def func(x):
    global res

    if x==n:
        res+=1
        return

    for y in range(n):
        if isused1[y] or isused2[x+y] or isused3[x-y+n-1]:
            continue
        isused1[y]=1
        isused2[x+y]=1
        isused3[x-y+n-1]=1
        func(x+1)
        isused1[y]=0
        isused2[x+y]=0
        isused3[x-y+n-1]=0
func(0)
print(res)



n이 15라서 풀 수 있는 하드코딩풀이
a= (0,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596)
print((a[int(input())]))



