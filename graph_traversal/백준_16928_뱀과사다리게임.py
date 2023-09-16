from collections import deque
n,m = map(int,input().split())
sa={}
snake={}
for i in range(n):
    x,y = map(int,input().split())
    sa[x]=y
for i in range(m):
    u,v=map(int,input().split())
    snake[u]=v
    
gragh=[0]*101

visit=[0]*101

def bfs(a):
    q=deque()
    q.append(a)
    while q:
        x=q.popleft()
        if x==100:
            return gragh[100]
        for i in range(1,7):
            nx=x+i
            if 0<nx<=100 and visit[nx]==0:
                if nx in sa:
                    nx=sa[nx]
                elif nx in snake:
                    nx=snake[nx]
                if visit[nx]==0:
                    visit[nx]=1
                    gragh[nx]=gragh[x]+1
                    q.append(nx)

x=bfs(1)                
print(x)

#메모리 : 34176 kb
#시간 : 64 ms
#코드길이 : 760 b
#풀이시간 : 약 1시간