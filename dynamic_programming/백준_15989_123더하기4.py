#실패
# 점화식 자체를 생각하기 힘들었다..
dp=[0]*10001

for i in range(3,10001):
    if i%2==0:
        dp[i]=dp[i-1]+2
    else:
        dp[i]=dp[i-1]+1
    
t = int(input())
for _ in range(t):
    x = int(input())
    print(dp[x])
    
# 코드길이 : 302 B
# 시간 :  ms
# 메모리 :  KB
