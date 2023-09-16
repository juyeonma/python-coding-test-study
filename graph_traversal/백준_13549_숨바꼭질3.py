# gragh초기화 값을 0에서 -1로만 바꾸어주니까 바로 성공했다.. 왜지?
from collections import deque
n,k = map(int,input().split())
gragh=[-1]*100001
gragh[n]=0
q=deque()
q.append(n)
cnt=0

while q:
    x=q.popleft()
    if x==k:
        print(gragh[x])
        break
    for nx in [x-1,x+1,x*2]:
        if 0<=nx<100001 and gragh[nx]==-1:
            if nx==x*2:
                gragh[nx]=gragh[x]
                q.appendleft(nx)
            else:
                gragh[nx]=gragh[x]+1
                q.append(nx)
                
#메모리 : 35364 kb
#시간 : 132 ms
#코드길이 : 444 b
#풀이시간 : 34분