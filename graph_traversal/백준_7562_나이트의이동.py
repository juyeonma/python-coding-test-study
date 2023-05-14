from collections import deque
t = int(input())
dx=[-2, -1, 1, 2, 2, 1, -1, -2] # 동서남북 대각선(4)
dy=[-1, -2, -2, -1, 1, 2, 2, 1]

def bfs(x,y,xx,yy):
        q=deque()
        q.append((x,y))
        visit[x][y]=1
        while q:
            qx,qy=q.popleft()
            if qx==xx and qy==yy: # 다음 위치가 목표 지점일때 이동 횟수를 출력하고 종료
                print(visit[xx][yy]-1)
                return
            for k in range(8):
                nx=qx+dx[k]
                ny=qy+dy[k]
                if 0<=nx<l and 0<=ny<l and visit[nx][ny]==0:
                    visit[nx][ny]=visit[qx][qy]+1
                    q.append((nx,ny))

for _ in range(t):
    l = int(input())
    x,y = map(int, input().split())
    xx,yy = map(int, input().split())
    visit=[[0]*l for _ in range(l)]
    bfs(x,y,xx,yy)
    
# 코드 길이 : 772 B
# 시간 : 1336 ms
# 메모리 : 34192 KB