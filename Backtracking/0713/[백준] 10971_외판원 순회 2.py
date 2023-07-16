# 백트래킹 접근 방법이 크게 두가지가 있는 것 같다 1번 풀이, 2번 풀이
# 1번 풀이는 배열에 넣고 빼면서 풀고 2번 풀이는 배열에 방문처리를 해서 푸는 방법이다
# 배열에 넣고 빼면서 풀면 비교적 코드가 간단해질 수있지만 방문했는지를 확인하는 if문에서 배열을 한번 더 돌기 떄문에
# 시간복잡도가 높아질 수 있다.

# 2번과 2번 수정코드의 차이는 arr.append후 arr.pop을 할때 cost를 함수 안에서 처리 할지 밖에서 처리할지의 차이이다
# 이 두 개 코드를 비교해보는 것도 백트래킹 이해도를 높일 수 있을 것 같다

# 처음에 0123 0132 ... 3210 까지 모두 백트래킹에 넣어서 풀었는데 시간초과가 났다
# 다시 처음도시까지 돌아올때까지의 최소 비용을 구하는 것이기 때문에 원형 배열의 느낌으로 생각하면 된다.
# 즉, 시작점은 어떤 도시가 됐든 하나로 지정하고 나머지 도시를 백트래킹 하면 된다

1번

n = int(input())
network = [list(map(int,input().split())) for _ in range(n)]
min_cost = 1000000*n # 최소비용을 담기위해 최대값 설정
arr = [0] # 첫번째 도시를 시작점으로 임의 지정

def func(cost):
    global min_cost
    if len(arr)==n and network[arr[-1]][arr[0]]: # 모든 도시를 거치고, 비용이 0이 아니라면
        cost+=network[arr[-1]][arr[0]] # 비용을 더해주고
        min_cost = min(min_cost,cost) # 최솟값 비교
        return
    
    for i in range(1,n): # 임의로 하나를 지정했기 떄문에 1번 도시부터 시작
        if i not in arr: # 거치지 않은 도시라면
            arr.append(i) # 해당도시를 방문처리하고
            if network[arr[-2]][arr[-1]]==0: # 다음도시로 갈때 0이면
                arr.pop() # 배열에서 빼고 
                continue # 다음 도시로 이동
            cost += network[arr[-2]][arr[-1]] # 비용을 더해주고
            func(cost) # 다음 depth의 도시로 이동
            cost -= network[arr[-2]][arr[-1]] # 해당 depth상태에서 다음 도시로 가기 위해 이전비용 빼주기
            arr.pop() # 배열에서 빼기

# func(0)
# print(min_cost)
# 1시간 17분
# 메모리 31256kb 시간 1068ms

1번 수정
n = int(input())
network = [list(map(int,input().split())) for _ in range(n)]
min_cost = 1000000*n
arr = [0]

def func(cost):
    global min_cost
    if len(arr)==n and network[arr[-1]][arr[0]]:
        min_cost = min(min_cost,cost+network[arr[-1]][arr[0]])
        return
    
    for i in range(1,n):
        if i not in arr and network[arr[-1]][i]:
            arr.append(i) 
            func(cost+network[arr[-2]][arr[-1]])
            arr.pop()

func(0)
print(min_cost)

#메모리 31256kb 시간 932ms


2번 
n = int(input())
network = [list(map(int,input().split())) for _ in range(n)]
min_cost = 1000000*n
vis = [0]*n
vis[0]=1

def func(depth,st,cost):
    global min_cost
    if depth == n and network[st][0]:
        min_cost = min(min_cost,cost+network[st][0])
        return
    
    for en in range(n):
        if not vis[en] and network[st][en]:
            cost+=network[st][en]
            vis[en]=1
            func(depth+1,en,cost)
            cost-=network[st][en]
            vis[en]=0

func(1,0,0)
print(min_cost)

#메모리 31256kb 시간 568ms



2번 수정
n = int(input())
network = [list(map(int,input().split())) for _ in range(n)]
min_cost = 1000000*n
vis = [0]*n
vis[0]=1

def func(depth,st,cost):
    global min_cost
    if depth == n and network[st][0]:  # 모든 도시를 다 돌았고, 마지막 도시에서 첫번째 도시가 0이 아니면
        min_cost = min(min_cost,cost+network[st][0]) # 마지막>첫번째 도시 비용 더해주고 최솟값 갱신
        return
    
    for en in range(1,n): # 첫번째 도시는 이미 정해뒀기 때문에 그다음도시부터 확인
        if not vis[en] and network[st][en]: # 방문안했고 갈수있는 도시라면
            vis[en]=1 # 방문처리하고
            func(depth+1,en,cost+network[st][en]) # 다음 depth로 들어가면서 비용 더해주기
            vis[en]=0 # 같은 depth에서 다른 도시로 가기 전 방문취소 처리, 나중에 다시 써야하니까

func(1,0,0)
print(min_cost)

#메모리 31256kb 시간 520ms