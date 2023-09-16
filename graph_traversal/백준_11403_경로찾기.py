#간선추가할 때, 양쪽에서 이어지는 것인 줄 알았는데 
#하나만 추가하면 됐었다.
from collections import deque
n = int(input())
num=[[] for _ in range(n)]

for i in range(n):
    x=list(map(int,input().split()))
    for j in range(n):
        if x[j]==1:
            num[i].append(j)
        
def bfs(a):
    visit=[0]*n
    q=deque()
    q.append(a)
    while q:
        x=q.popleft()
        for nx in num[x]:
            if visit[nx]==0:
                visit[nx]=1
                q.append(nx)
    return visit

for i in range(n):
    result=bfs(i)
    for j in range(n):
        print(result[j],end=' ')
    print()
    
#메모리 : 34140 kb
#시간 : 80 ms
#코드길이 : 597 b
#풀이시간 : 30분(대충)