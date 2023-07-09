from collections import deque
n = int(input())
a,b = map(int,input().split())
m = int(input())
fam=[[] for _ in range(n+1)]
visit=[0]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    fam[x].append(y)
    fam[y].append(x)

def bfs(aa):

    q=deque()
    q.append(aa)
    while q:
        xx=q.popleft()
        for i in fam[xx]:
            if visit[i]==0:
                visit[i]=visit[xx]+1 #거리구하는 거랑 같은 것 같다
                q.append(i)

bfs(a)
if visit[b]==0:
    print(-1)
else:
    print(visit[b])
# 시간 : 64 ms
# 메모리 : 34140 KB