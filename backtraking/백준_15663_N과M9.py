n,m = map(int, input().split())
num = list(map(int,input().split()))

s=[]
num.sort()
ans=[]
visit=[0]*n #리스트에 있는 숫자를 중복이어도 다 써야함
def dfs():
    if len(s)==m:
        ans.append(s[:])
        return
    for i in range(len(num)):
        if visit[i]==0:
            visit[i]=1
            s.append(num[i])
            dfs()
            visit[i]=0
            s.pop()

dfs()
ans = sorted(list(set(map(tuple,ans))))
for i in ans:
    print(*i,sep=' ')

# 시간 : 423 ms
# 메모리 : 41332 KB