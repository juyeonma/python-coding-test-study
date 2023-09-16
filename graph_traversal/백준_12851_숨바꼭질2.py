# 다시풀기
from collections import deque
n,k=map(int,input().split())
gragh=[0]*100001
visit=[0]*100001

cnt=0
res=0
q=deque()

def bfs(a):
    global res,cnt
    q.append(a)
    while q:
        x=q.popleft()
        temp=gragh[x]
        if x==k:
            cnt+=1
            res=temp
            continue
        for nx in [x-1,x+1,2*x]:            
            if 0<=nx<100001 and (gragh[nx]==0 or gragh[nx]==gragh[x]+1):
                gragh[nx]=gragh[x]+1
                q.append(nx)
    return res,cnt
                
x,y=bfs(n)
print(x)
print(y)

#메모리 : 38468 kb
#시간 : 380 ms
#코드길이 : 547 b
#풀이시간 : 53분