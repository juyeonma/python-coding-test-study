# 함수로 bfs를 만드니 시간이 엄청 단축됐다.
# 메모리를 절약하려고 딕셔너리로 구했는데 메모리가 엄청 크게 나왔다.
# 딕셔너리는 해시라서 배열보다 메모리가 많이 들긴하는데 빈 배열 공간보다 많이 들지는 몰랐다.

# 예전에 풀어본 bfs 유형인듯 하다

from collections import deque

f,s,g,u,d = map(int,input().split())
vis = {}
answer = "use the stairs"
vis[s]=0
q= deque([s])
while q:
    x=q.popleft()
    for dir in [u,-d]:
        nx=x+dir
        if nx<1 or nx>f:
            continue
        if nx in vis:
            continue
        vis[nx]=vis[x]+1
        q.append(nx)

if g in vis:
    answer=vis[g]
print(answer)

#메모리 137924kb 시간 944ms


from collections import deque

f,s,g,u,d = map(int,input().split())
vis = {}
answer = "use the stairs"
vis[s]=0
q= deque([s])
def bfs():
    while q:
        x=q.popleft()
        for dir in [u,-d]:
            nx=x+dir
            if nx<1 or nx>f:
                continue
            if nx in vis:
                continue
            vis[nx]=vis[x]+1
            q.append(nx)
bfs()
if g in vis:
    answer=vis[g]
print(answer)

#18분
#메모리 137856kb 시간 544ms