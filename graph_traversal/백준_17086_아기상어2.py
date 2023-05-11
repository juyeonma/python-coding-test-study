from collections import deque
n, m = map(int, input().split())
gragh=[]
for _ in range(n):
    gragh.append(list(map(int, input().split())))

#dfs가 익숙한데 dfs로는 못 푸는 걸까
def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx=[0, 0, 1, -1, -1, 1, 1, -1] # 동서남북 대각선(4)
    dy=[-1, 1, 0, 0, -1, -1, 1, 1]
    visit=[[0]*m for _ in range(n)]
    visit[x][y]=1
    while q:
        px,py = q.popleft()
        for i in range(8):
            nx=px+dx[i]
            ny=py+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and visit[nx][ny]==0:
                visit[nx][ny]=visit[px][py]+1
                q.append((nx,ny))
                if gragh[nx][ny]==1:
                    return visit[nx][ny]-1

max_cnt=[]
for i in range(n):
    for j in range(m):
        if gragh[i][j]==0:
            max_cnt.append(bfs(i,j))
print(max(max_cnt))

# 코드 길이 : 877 B
# 시간 : 3446 ms
# 메모리 : 34129 KB