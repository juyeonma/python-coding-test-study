# 저번이랑 똑같은 방식으로 한 것 같은데... 바로 풀렸다..
# 점프문제랑 같은 유형이 맞는 것 같다

# 맨 왼쪽위부터 시작해서 오른쪽과 아래쪽으로 이동하면서 우유를 마신다
# 그러므로 bfs방향은 두가지만 가능
# for문을 돌면서 0이 되는 부분을 찾는다 왜냐하면 영학이는 딸기우유를 먼저 마셔야하기 때문이다
# 찾으면서 방문하지 않았던 곳이라면 1으로 초기화하고 방문했던 곳이라면 그대로 둔다
# 그리고 오른쪽으로 이동한 경우 아래로 이동한 경우를 나눠서 구한다.
# 현재까지 먹은 우유의 개수의 %3을 한 것과 다음에 방문할 위치가 같으면 비교를 통해 갱신한다
# 우유먹는 순서는 정해져 있고, 3으로 나눠서 나머지를 구하면 그것이 다음에 먹어야 할 우유의 숫자이다

#이렇게 갱신하고 먹어야할 우유가 아니라면 현재 있는 값과 그 이전값 중 최대 갑승로 갱신한다

# 생각해보니 이건 bfs로 푼 것 같다.
# 물론 이전의 값을 통해 다음값을 구한다는 점에서 dp로 볼 수 있지만, 아래에 dp스럽게 푼 풀이가 있다
n = int(input())
city = [list(map(int,input().split())) for _ in range(n)]

vis = [[0]*n for _ in range(n)]
dx=[1,0]
dy=[0,1]

for i in range(n):
    for j in range(n):
        if city[i][j]==0:
            vis[i][j]=max(vis[i][j],1)
        for dir in range(2):
            nx = i+dx[dir]
            ny = j+dy[dir]
            if nx>=n or ny>=n:
                continue
            if city[nx][ny]==vis[i][j]%3:
                vis[nx][ny]=max(vis[nx][ny],vis[i][j]+1)
            else:
                vis[nx][ny]=max(vis[nx][ny],vis[i][j])

print(vis[-1][-1])
# 메모리57764kb	시간 1992ms


# 이 풀이가 확실히 더 dp에 가깝다
# 시간이 가장 빠른 분의 풀이인데 갱신의 메커니즘은 내 풀이와 같은데 훨씬 최적화 시킨 풀이이다
# 해당 위치로 올 수 있는 두 개의 이전 위치의 dp를 비교해서 큰 값을 현재 위치에 넣는다
# 그리고 그 값%3이 바나나우유의 숫자와 같으면 카운팅을 한다

# 그래도 만약 실전이었다면 나는 bfs로 풀었을 것 같다. 물론 시간복잡도상에서 안전해서 어떤 풀이든 상관없다
# 아직 dp풀이는 완전히 와닿지는 않는 것 같다

n = int(input())
city = [list(map(int,input().split())) for _ in range(n)]
dp=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        if dp[i][j]%3==city[i-1][j-1]:
            dp[i][j]=dp[i][j]+1

print(dp[-1][-1])

# 메모리 55600kb 시간 808ms

# bfs는 오른쪽 아래쪽을 검사해야돼서 2배많은 공간을 탐색해야하고 if문 등의조건이 있어서 이정도 차이가 난 것 같다