# 스스로는 풀 지 못했지만 완전 보고 풀지는 않았다.
# 어디서 최대가 나올지 모르므로 모든 경우를 모두 검사해야한다.
# 2배가 되는 부분을 기준으로 이동하며 구하는데 기준위치와 부메랑읻 될수있는 날의 위치가 
# 나무 재료 안에서 만들어질수있는지를 판단하면서 구해나간다

# 가능하면 그 부분들을 방문처리해주고 그 다음 위치를 확인하는 방식으로 백트래킹을 하면서 구한다

n,m = map(int,input().split()) # 세로와 가로길이를 입력받기
wood = [list(map(int,input().split())) for _ in range(n)] # 나무 판자 크기 입력받기
vis = [[0]*m for _ in range(n)] # 방문처리 하기 위해 입력받기
dx = [0,1,0,-1,0] # 2배가 될 수 있는 부분을 기준으로 가능한 위치 정하기
dy = [1,0,-1,0,1] # dx,dy의 5번째 위치는 첫번째 인덱스와 같음. (0번 1번) (1번 2번).. 묶으면서 구하기 위해 이렇게 했습니다
max_s = 0 # 각 경우의 수마다 최대값이 무엇인지 구하기 위한 변수

def func(x,y,s):
    global max_s 
    
    if y>=m: # 가로길이를 넘어가게 되면 그 다음줄로 가기
        x+=1
        y=0
    if x>=n: # 판자를 벗어나게 되면
        max_s = max(max_s,s)   # 최대값 확인
        return
    if not vis[x][y]: # 방문되지 않았다면
        for dir in range(4): # 각 방향마다 확인
            nx1 = x+dx[dir]
            ny1 = y+dy[dir]
            nx2 = x+dx[dir+1]
            ny2 = y+dy[dir+1]
            if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m: # 모두 판자안이면서
                if not vis[nx1][ny1] and not vis[nx2][ny2]: # 방문되지 않았다면
                    temp=s+wood[x][y]*2 # 기준위치는 두배로하고
                    vis[x][y]=1 #방문처리 후 
                    temp+=wood[nx1][ny1] # 나머지 위치 더하기
                    temp+=wood[nx2][ny2] 
                    vis[nx1][ny1]=1 # 방문처리
                    vis[nx2][ny2]=1 
                    func(x,y+1,temp) # 그 다움위치 확인하기
                    vis[x][y]=0 # 끝까지 모두 확인한 후 다시 방문취소
                    vis[nx1][ny1]=0
                    vis[nx2][ny2]=0
    func(x,y+1,s) # 갈 수있는 곳이지만 가지 않고 다음 위치를 확인하기 위한 재귀
 
if n<2 or m<2:  # 나무 재료 크기가 작을경우
    print(0)
else:
    func(0,0,0)
    print(max_s)