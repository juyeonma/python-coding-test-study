from collections import deque
n,k = map(int, input().split())
s = list(map(int, input().split()))

visit=set() #dic()

q=deque()

for i in s:
    q.append((i,1))
    visit.add(i) #방문한지를 visit리스트 안에 있는지 확인
    
result=0
home=0

while q:
    now, b = q.popleft()
    for i in [1,-1]:
        nx= now+i
        if nx in visit:
            continue
        visit.add(nx)
        result+=b
        home+=1
        q.append((nx,b+1)) #방문 직전에 있는 위치에서 1을 더해줘서 불행도를 저장
        if home==k:
            q=list()
            break
print(result)

# 코드 길이 : 550 B
# 시간 : 276 ms
# 메모리 : 58560 KB

### dic로 해결한다면,,?
from collections import deque
n,k = map(int, input().split())
s = list(map(int, input().split()))

visit=dict() #dic()

q=deque()

for i in s:
    q.append((i,1))
    visit[i]=0 #샘물은 방문하지 않음
    
result=0
home=0

while q:
    now, b = q.popleft()
    for i in [1,-1]:
        nx= now+i
        if nx in visit:
            continue
        visit[nx]=visit[now]+1
        result+=b
        home+=1
        q.append((nx,b+1)) #방문 직전에 있는 위치에서 1을 더해줘서 불행도를 저장
        if home==k:
            q=list()
            break
print(result)

# 코드 길이 : 589 B
# 시간 : 276 ms
# 메모리 : 63256 KB