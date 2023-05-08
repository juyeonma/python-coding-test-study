#음..
from collections import deque
import sys

input = sys.stdin.readline

def bfs(g): # 선거구를 뽑음
    q = deque()
    check=[0 for _ in range(n)]
    q.append(g[0])
    check[g[0]]=1 #방문했음을 확인
    cnt,ans = 1,0
    while q:
        x = q.popleft()
        ans+=p[x] #각 구역의 인원을 합함
        for nx in a[x]: #인접한 구역을 확인
            if nx in g and not check[nx]: #인접한 구역이 방문하지 않은 곳이라면
                check[nx]=1 #1로 바꾸어줌
                cnt+=1 #지역구를 추가
                q.append(nx) #다음 구역을 탐색
    if cnt==len(g): #지역구 개수가 같아지면 
        return ans
    else:
        return 0
    
def dfs(cnt, x, end): # 선거구가 이어져 있는지 확인
    global min_ans
    #원하는 구역의 개수만큼 도달했으면
    if cnt==end:
        g1,g2=deque(), deque() #큐 만들기
        for i in range(n):
            if c[i]: #방문하지 않은 곳이라면
                g1.append(i)
            else:
                g2.append(i)
        ans1 = bfs(g1) #g1의 값이 인접한 값인지 확인
        if not ans1:
            return
        ans2 = bfs(g2) #g2 값이 인접한지 확인
        if not ans2:
            return
        min_ans = min(min_ans, abs(ans2-ans1)) #인구 차의 최소값을 저장
        return
    for i in range(x,n):
        if c[i]:
            continue
        c[i]=1
        dfs(cnt+1,i,end)
        c[i]=0

n = int(input())
p = list(map(int, input().split()))
a = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(1,x[0]+1):
        a[i].append(x[j]-1)
        
min_ans = sys.maxsize
for i in range(1,n//2+1): #구역을 몇대 몇으로 나눌지(n//2까지만 하면됨)
    c=[0 for _ in range(n)]
    dfs(0,0,i)
if min_ans == sys.maxsize:
    print(-1)
else:
    print(min_ans)
    

#코드길이 : 1339 B
#시간 : 72 ms