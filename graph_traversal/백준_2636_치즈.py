from collections import deque
n,m = map(int,input().split())
cheese = []
for _ in range(n):
    cheese.append(list(map(int, input().split())))

dx=[0,0,1,-1]
dy=[-1,1,0,0]

ans = []

def bfs():
    q=deque()
    q.append((0,0))
    visit[0][0]=1
    cnt=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
                if cheese[nx][ny]==0: #치즈가 없는 곳으로 이동한다면
                    visit[nx][ny]=1 #그곳을 방문처리
                    q.append((nx,ny)) #치즈가 아닌 부분을 큐에 넣음
                elif cheese[nx][ny]==1: #치즈가 있는 곳을 탐색하게 된다면
                    cheese[nx][ny]=0 #녹아서 없어질 예정이니까 0으로 바꿔줌
                    visit[nx][ny]=1 #방문처리
                    cnt+=1 #안쪽 치즈까지 녹게 되므로 1만 플러스
    ans.append(cnt) #최종적인 카운트 값을 ans에 저장
    return cnt

time=0
while 1:
    time +=1
    visit=[[0]*m for _ in range(n)]
    cnt=bfs()
    if cnt==0: #치즈가 다 녹아서 셀 cnt가 없으면
        break
print(time-1) #모두 녹는 시간
print(ans[-2]) #그 전에 남았던 시간


# 코드 길이 : 847 B
# 시간 : 92 ms
# 메모리 : 34324KB