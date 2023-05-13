# bfs로 공주위치까지 가는 경우를 찾고 검위치를 따로 구해서 검위치를 통해 가는 경우와 비교하여 최솟값을 뽑는다.
# 풀긴했지만 반례를 생각하는 것이 너무 어렵다.
# 코테에서는 스스로 반례를 찾아야 할텐데 걱정이 된다.
# 반례를 잘찾는 방법은 뭘까?

from collections import deque

n,m,t = map(int,input().split())

tower = [list(map(int,input().split())) for _ in range(n)]
vis = [[0 for _ in range(m)] for _ in range(n)]
queue =deque([(0,0)]) # 처음 위치를 큐에 넣는다

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(q):
    gram_x=0
    gram_y=0
    flag=False
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x+dx[dir]
            ny = y+dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=m: # 범위벗어나면 탈출
                continue
            if vis[nx][ny] or tower[nx][ny]==1: # 방문한곳과 벽이 있으면 탈출, 원래는 처음 위치를 1로 만들어야하지만 이 문제 특성상 bfs를 통해 다시 첫위치로 가도 다른 요소에 영향을 미치지 않기 때문에 이렇게 했다. 
                continue
            if tower[nx][ny]==2:  # 검의 위치 체크
                gram_x=nx
                gram_y=ny
                flag=True   # 검의 위치까지 갈 수있는지 체크
            vis[nx][ny]=vis[x][y]+1 
            q.append((nx,ny))
    time=10001  # 최대값 초과로 초기화
    if vis[n-1][m-1]: # 공주위치까지 간다면
        time=vis[n-1][m-1]  # bfs만으로 나오는 최소값
    if flag:  # 검의 위치까지 간다면
        time=min(time,vis[gram_x][gram_y]+abs(n-1-gram_x)+abs(m-1-gram_y))  # 검의위차와 순수bfs 최소값 
    if time<=t: # 최종 시간이 제한시간 이내라면
        return time # 시간 출력
    else:
        return "Fail" # 제한시간 이내가 아니거나 공주위치까지 갈 수없다면 fail출력

print(bfs(queue))

# 더 최적화풀이 생각해보기