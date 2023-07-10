# 전형적인 bfs/dfs 문제인데 너무 오래걸렸다.
# dfs로 풀어보고 싶었는데 어떻게 풀지 감이 안와서 그냥 bfs로 풀었다.

from collections import defaultdict
from collections import deque

n = int(input())
x,y = map(int,input().split())
m = int(input())
relationship = defaultdict(list)
vis = [0]*(n+1)
count=0
q = deque()
for _ in range(m):
    a,b = map(int,input().split())
    relationship[a].append(b)
    relationship[b].append(a)

vis[x]=1
q.append(x)

while q:
    temp = q.popleft()
    for i in relationship[temp]:
        if not vis[i]:
            q.append(i)
            vis[i]=vis[temp]+1

if vis[y]:
    print(vis[y]-1)
else:
    print(-1)

# 메모리 34160kb 시간 64ms
# 걸린시간 40분


n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
vis = [False] * (n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v,cnt):
    if v==b:
        print(cnt)
        return
    
    for i in graph[v]:
        if not vis[i]:
            vis[i]=True
            dfs(i,cnt+1)

vis[a]=True
dfs(a,0)
if not vis[b]:
    print(-1)

# 메모리 31256kb 시간 44ms