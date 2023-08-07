# 런타임 에러,,
# 이거는 다시 보면 해결할 수 있지 않을까..
n = int(input())
grape=[]
for _ in range(n):
    grape.append(int(input()))
    
dp=[0]*n
dp[0]=grape[0]
dp[1]=grape[0]+grape[1]
dp[2]=max(grape[0]+grape[2],grape[1]+grape[2], dp[1])
for i in range(3,n):
    dp[i]=max(dp[i-1],grape[i]+dp[i-2],grape[i]+grape[i-1]+dp[i-3])
print(max(dp))

# 코드길이 : 302 B
# 시간 :  ms
# 메모리 :  KB

