#다시 한번 봐보기
from collections import deque

#양쪽으로 회전이 가능한지 확인하는 함수
def rot_r(n,r):
    if n>4 or t[n-1][2]==t[n][6]:
        return
    if t[n-1][2]!=t[n][6]: #같지 않으면 회전 가능
        rot_r(n+1,-r) # 연결된 모든 톱니 확인
        t[n].rotate(r) #회전

def rot_l(n,r):
    if n<1 or t[n][2]==t[n+1][6]:
        return
    if t[n][2]!=t[n+1][6]:
        rot_l(n-1,-r)
        t[n].rotate(r)

t={}
for i in range(1,5):
    t[i]=deque(map(int,input()))
    
k = int(input())

for _ in range(k):
    n,r = map(int,input().split())
    # 톱니 회전 가능한지 확인
    rot_r(n+1,-r)
    rot_l(n-1,-r)
    t[n].rotate(r) #회전
    
ans=0
for i in range(4):
    ans+=t[i+1][0]*(2**i)
print(ans)

# 메모리 : 34176 KB
# 시간 : 68 ms
# 코드길이 : 569 B