# 치킨집 모두 배열에 넣어서 M개만큼 조합으로 만들기
# 하나의 경우씩 치킨집의 위치를 큐에 넣기
# 집까지의 거리 최소값 갱신
# 다시 다 돌면서 집 위치에서 카운팅 
# 모든 조합을 끝내고 최소값 출력 

# 힙겹게 다 풀었는데 시간초과가 났다.
# 딱봐도 bfs처럼보였고 시간초과도 안날것같았는데 보기좋게 시간초과가 났다. 왜시간초과가 났을지가 궁금하다
# 결국 답을 봤고, 완전히 보지는 않고 bfs가 아닌 것만 확인하고 풀었다.
# 풀고나니 맞춘 풀이가 훨씬 효율적이라는 것을 알았다. bfs는 전부 다 돌아야하지만, 치킨집과 집의 위치만을 이용해서 구하면 이들 좌표만 검사하면 되기때문이다.
# 좌표와 이동해야한다에 꽂혀서 bfs로 풀었는데 고정관념을 가지면 안되겠다.

# from itertools import combinations
# from collections import deque

# N,M = map(int,input().split())
# board = [list(map(int,input().split())) for _ in range(N)]
# house=[]
# chicken=[]
# dx=[0,0,1,-1]
# dy=[1,-1,0,0]
# min_distance=1500

# for i in range(N):
#     for j in range(N):
#         if board[i][j]==1:
#             house.append((i,j))
#         if board[i][j]==2:
#             chicken.append((i,j))

# c= combinations(chicken,M)

# for case in c:
#     check=set(case)
#     queue =deque(case)
#     vis=[[0]*N for _ in range(N)]

#     while queue:
#         x,y=queue.popleft()
#         for dir in range(4):
#             nx = x+dx[dir]
#             ny = y+dy[dir]
#             if nx<0 or ny<0 or nx>=N or ny>=N:
#                 continue
#             if (nx,ny) in check:
#                 continue
#             if vis[nx][ny] and vis[nx][ny]<vis[x][y]+1:
#                 continue
#             else:
#                 vis[nx][ny]=vis[x][y]+1
#             queue.append((nx,ny))
#     temp=0
#     for x,y in house:
#         temp+=vis[x][y]
#     min_distance=min(min_distance,temp)

# print(min_distance)

from itertools import combinations

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
house = []
chichen=[]

for i in range(N):  #도시를 돌면서 집의 위치와 치킨집의 위치를 찾는다
    for j in range(N):
        if board[i][j]==1:
            house.append((i,j))
        if board[i][j]==2:
            chichen.append((i,j))

c = combinations(chichen,M) # 치킨집의 일부만 선택하는 것이기때문에 조합을 이용한다
result=1500 #N의 최대가 50이기 때문에 끝점에 있을 경우 거리가 99이다 치킨집은 13개까지 선택이 가능하므로 1300보다 적은 수가 최대값인데 그냥 1500으로 했다
for case in c:  #치킨집 위치의 경우의수
    min_distance=0    #한 조합이 끝날때마다 갱신할 최소 거리
    for a,b in house:   # 조합 속에서 집과 모든 치킨집 중 최소거리
        temp=101        # 99가 최대겠지만 그냥 101로 했다
        for c,d in case:    # 고른 조합속의 치킨집들
            temp=min(temp,abs(a-c)+abs(b-d))  # 최소값 구하기
        min_distance+=temp #집과 치킨집과의 최소거리 카운팅
    result=min(result,min_distance) # 한 조합이끝날때마다 다른 조합에서 나온 최소값과 비교

print(result)
    