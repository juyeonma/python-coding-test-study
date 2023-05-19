import sys
input = sys.stdin.readline
n,m = map(int,input().split())
friend=[[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

visit=[0]*n
ans=False
def bfs(idx,y):
    global ans
    visit[idx]=1
    if y==4:
        ans=True
        return
    for i in friend[idx]:
        if visit[i]==0:
            visit[i]=1
            bfs(i,y+1)
            visit[i]=0 #방문표시를 해제하여 다른 친구와의 관계가 가능하게 함

for i in range(n): #각각의 친구들을 탐색
    bfs(i,0)
    visit[i]=0
    if ans:
        break
if ans:
    print(1)
else:
    print(0)


# 코드 길이 : 658 B
# 시간 : 1952 ms
# 메모리 : 31256 KB