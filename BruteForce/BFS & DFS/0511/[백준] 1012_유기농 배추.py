#전형적인 bfs문제였다. 함수가 생각나서 함수로 빼려는 노력을 담아보았다.
# deque를 사용할 때 deque((nx,ny))이렇게 해서 오류가 났는데 deque([(nx,ny)])이렇게 해야된다...

from collections import deque

T = int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]

for _ in range(T):    #케이스별로 구하기 위한 for문
    M,N,K = map(int,input().split())
    land = [[0]*N for _ in range(M)]
    for _ in range(K):      # 배추위치에 배열처리해주기
        x,y=map(int,input().split())
        land[x][y]=1
    
    vis=[[0]*N for _ in range(M)]   #방문한곳은 다시 방문안하기 위한 배열
    min_bug=0   # 최소 지렁이 개수

    def bfs(q):
      while q:
        x,y=q.popleft()
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if nx<0 or ny<0 or nx>=M or ny>=N:  # 공간이탈 시 continue
              continue
            if vis[nx][ny] or not land[nx][ny]:  #이미 방문했거나 배추없는 공간일 때 continue
                continue
            vis[nx][ny]=1
            q.append((nx,ny))

    for i in range(M):
        for j in range(N):
            if vis[i][j] or not land[i][j]:   # bfs로 방문처리된곳이면 넘어가고 땅에 아무것도 없어도 넘어가기
                continue
            queue=deque()
            queue.append((i,j))
            vis[i][j]=1
            bfs(queue)  # 배추위치 파악하고 
            min_bug+=1  # bfs끝나면 벌레 하나 추가
    print(min_bug)