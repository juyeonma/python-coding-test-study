import sys
from collections import deque
input = sys.stdin.readline
r, c, n = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
def check():
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                q.append((i, j))
            else:
                board[i][j] = 'O'
def bomb():    
    while q:
        x, y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= r or 0 > ny or ny >= c:
                continue

            board[nx][ny] = '.'

for i in range(n-1):
    if i % 2 == 1:
        bomb()
    else:
        check()

for i in range(r):
    print(''.join(board[i]))

# 메모리 : 35756	시간 : 1668ms
# 오.. 예전에 풀때는 못풀었던것같은데.. 이번에는 풀었다..!
# 실력이 점점 느는 것 같기도?!..