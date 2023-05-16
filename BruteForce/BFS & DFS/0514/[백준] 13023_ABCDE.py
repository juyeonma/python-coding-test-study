# 문제를 보고 dfs랑 백트래킹을 써야된다는 것을 알았다.
# 재귀가 이해가 안가서 늘 그냥 미뤄만 두고 넘어갔던 유형인데 이 문제를 풀기 위해서 공부를 했다
# 아이디어는 떠올렸지만 아직 백트래킹이 약해서 못풀었다. 하지만 익숙해지다보면 풀 수 있을 것 같다.

# 문제에 나온친구관계가 존재한다면 바로 재귀를 탈출하기 위해 sys.exit()를 사용했고 만약 여기서 종료되지 않는다면 코드가 끝까지 실행된 것이고, 5명의 친구관계과 이루어지지 않은 것이므로 마지막 부분에 0을 출력하게 하였다.

#어디서부터 시작해야 5명의 친구가 만들어질지 확인할 수 없으므로 완전탐색으로 모든 사람들을 시작점으로 dfs를 돌릴 수있게하였다.
# 각 사람마다 dfs를 돌리면서 친구관계 5명이 이루어지면 1을 출력하고 종료한다.

# bfs나 dfs나 백트래킹이나 모두 기본틀을 알고 있는 것이 중요한 것 같다.
# 앞으로 BFS로도 풀어보고 dfs로도 풀어보는 습관을 가져야겠다

# import sys

# n,m = map(int,input().split())
# vis=[0]*2001    #백트래킹에서 방문 표시
# relationship = [[] for _ in range(n)]

# for _ in range(m): # 각 관계를 배열에 넣기
#     a,b = map(int,input().split())
#     relationship[a].append(b)
#     relationship[b].append(a)

# def dfs(idx,depth): # 백트래킹으로 확인
#     vis[idx]=1  # 첫번째 위치 방문 표시
#     if depth==4: # depth는 0부터 시작했으므로 4명만 더 확인하면 되니까 4가되면 탈출
#         print(1)
#         sys.exit()
#     for i in relationship[idx]: # 친구관계 확인
#         if vis[i]:  # 이미 방문한 곳이라면 넘어가기
#             continue
#         vis[i]=1    # 방문안했기 때문에 방문표시
#         dfs(i,depth+1)  # 더 깊이 들어가기
#         vis[i]=0    # 윗줄을 넘어왔다는건 하나의 깊이우선탐색루트를 끝냈다는 것이므로 다시 방문 표시 해제 (이거 맞는 말일까요?)

# for i in range(n):  # 어디서 시작해야 5명이 만들어질지 모르므로 모든 사람에 대하여 반복
#     dfs(i,0)
#     vis[i]=0

# print(0)


# dfs와 백트래킹을 이해하기위해 vis없이도 풀어보았다.
# 백트래킹을 완벽하게 이해했다고는 할 수 없지만 조금 알게 된 것 같다.  
import sys
n,m = map(int,input().split())
relationship = [[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    relationship[a]+=[b]
    relationship[b]+=[a]

friends=[]

def dfs(k):
    if len(friends)==5:
        print(1)
        sys.exit()

    for i in relationship[k]:   
        if i in friends:    #배열이기 때문에 여기서 한번더 돌면서 찾게 돼서 기존 풀이보다 느리다
            continue
        friends.append(i)
        dfs(i)
        friends.pop()


for i in range(n):
    friends=[]
    friends.append(i)
    dfs(i)

print(0)