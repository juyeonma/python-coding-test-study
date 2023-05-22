# 16분
# 메모리 34192kb 시간 1188ms
# 이문제는 자바스크립트로 풀어본적이 있었다.
# dx,dy가 다르다는 점을 빼면 이전문제들과 똑같은 것 같다.
# 함수로 만들어두고 이 함수에서 여기까지 만들거다라고 생각하고 전역코드들을 짜니까 구조가 더 잘 잡히는 느낌이다.
# 현재 위치에서부터 bfs를 돌리면 다음위치는 무조건 최소값이 들어가게 된다. 그래서 최소를 새롭게 갱신할 필요없이 bfs를 돌리다가
# 도착위치를 if문으로 확인한 후 해당 위치에서의 값-1을 리턴하면 된다.
# 그리고 출발지가 도착지일 수 있기 때문에 queue를 돌리기 전에 같은지 확인하는 코들르 작성해둬야한다.
# 출발지를 1로 둔이유는 0으로 둘 경우에는 bfs를 돌다가 출발지 위치에 왔을때 새롭게 값을 갱신할수있기 때문에 그냥 1로 둔 후 -1을 했다.

from collections import deque

T = int(input())
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,-1,1]

def bfs(st_x,st_y,des_x,des_y,size):
    queue=deque()
    queue.append((st_x,st_y))
    board[st_x][st_y]=1
    if st_x==des_x and st_y==des_y:
        return 0
    while queue:
        x,y=queue.popleft()
        for dir in range(8):
            nx,ny=x+dx[dir],y+dy[dir]
            if nx<0 or ny<0 or nx>=size or ny>=size:
                continue
            if board[nx][ny]:
                continue
            board[nx][ny]=board[x][y]+1
            queue.append((nx,ny))
            if nx==des_x and ny==des_y:
                return board[nx][ny]-1

for _ in range(T):
    I = int(input())
    board = [[0]*I for _ in range(I)]
    st_x,st_y=map(int,input().split())
    des_x,des_y=map(int,input().split())
    result=bfs(st_x,st_y,des_x,des_y,I)
    print(result)