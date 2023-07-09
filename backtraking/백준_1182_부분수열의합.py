n,s = map(int, input().split())
num = list(map(int,input().split()))
cnt=0
lst=[]
visit=[0]*n

def dfs(start):
    global cnt
    if sum(lst)==s and len(lst)>0: #카운트 조건을 만족
        cnt+=1
        
    for i in range(start,n): #중복 조합이 허락되지 않음
        if visit[i]==0:
            visit[i]=1
            lst.append(num[i])
            dfs(i+1)
            visit[i]=0
            lst.pop()
            
dfs(0)

print(cnt)

# 시간 : 389 ms
# 메모리 : 31256 KB