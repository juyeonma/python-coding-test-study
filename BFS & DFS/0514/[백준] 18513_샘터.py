# 샘터의 위치가 정해져있는 것이지 집의 위치는 정해져있지않아서 메모리초과가 났다.
# 집의 위치를 고려해서 대충 공간을 3억으로 했더니 통과되었지만 시간이 너무 오래걸려서
# 집의 개수 10만개, 경계값에서 샘터가 있을때 100000000이므로 마이너스 플러스 1억 십만으로 2억 이십만 1 로 바꿨는데도 메모리초과가 났다.0

# 그 위치를 넘어갈수가 없을 거라고 생각하는데 왜 메모리초과가 나는걸까.. 이해가 안가는데 아시는 분 알려주세요

# 메모리 43252KB 시간 4252ms
# 다른 사람들에 비해서 메모리는 적게 사용했지만 시간이 너무 오래걸렸다.

# 두번째 풀이는 다른 분의 풀이인데 나의 풀이는 처음에 방문배열을 만들어줘야되고, 길이도 길기때문에
# 시간이 더 오래 걸린 것 같다. 배열을 만들대 3억의 길이인데 이미 시간초과인 것 같은데 왜 돌아갔을까?
# 1초에 1억번 연산을 할 수있다고 알고있는데 더 많이 할 수 있었던 건가보다 (10억번이라고 들은 것 같기도 한데 10억 번인가?)


# 이문제를 bfs인걸 모르고 풀었다면 풀 수 있었을까? 풀 수있을 것 같긴 한데 무슨 유형인지 알고 푸니까 더 사고의 흐름이 빨라진 것 같다.
# bfs를 생각하면 배열이 먼저 생각난다. 그래서 나는 그렇게 생각을 깊이하지않고 집과 샘터의 공간을 배열로 선언했다. 풀긴했지만 비효율적인 것 같다.
# bfs는 너비우선탐색이고 이 정의를 기반으로 자유롭게 생각해야 하는데 항상 이중배열에 네 방향으로 가는 문제만 풀어서 사고가 고착화된 것 같다. 꼭 배열이 아니더라도 bfs를 적용할 수 있음을 기억하자

from collections import deque

n,k = map(int,input().split())
water=list(map(lambda x:int(x)+150000000,input().split())) # 음수의 샘터의 위치를 배열에 담기위해서 변환
vis=[0]*300000000 # 집의 위치를 고려해서 넉넉하게 3억정도로 잡았습니다.
water_set=set() # bfs를 돌면서 샘터의 위치라면 넘어갈수있게 set에 담습니다.
for v in water: 
    water_set.add(v)
ans=0 # 불행도 
cnt=k # 집의 개수 만큼의 큐를 돌리기 위한 변수
def bfs(cnt,ans):
    queue = deque(water)
    while queue:
        x=queue.popleft()
        for dir in [1,-1]:
            nx=x+dir
            if nx in water_set: #샘터의 위치라면 continue
                continue
            if vis[nx]: # 방문한 곳이라면 continue
                continue
            vis[nx]=vis[x]+1  #불행도 설정
            ans+=vis[nx]  # 집위치선정후 불행도 누적
            cnt-=1  # 집위치를 선정할때마다 cnt-=1
            queue.append(nx)
            if cnt==0:  # 집의 개수만큼 모두 불행도를 구햇으면 
                return ans  # 불행도 리턴

# print(bfs(cnt,ans)) 

# 메모리 58464KB 시간 204ms
# from collections import deque

n,k = map(int,input().split())
n_list = list(map(int,input().split()))
visit=set()
queue=deque()
for i in n_list:
    queue.append((i,0))
    visit.add(i)

ans = 0
cnt = k
def bfs(cnt,ans):
    while queue:
        x,d=queue.popleft()
        for dir in [-1,1]:
            nx=x+dir
            if nx in visit:
                continue
            queue.append((nx,d+1))
            visit.add(nx)
            ans+=d+1
            cnt-=1
            if not cnt:
                return ans
        
print(bfs(cnt,ans))