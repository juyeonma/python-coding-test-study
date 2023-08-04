# dp 정의할 때, 제한값만큼 하면 될 줄 알았는데 그냥 입력 값 n,t만큼 사이즈를 만들면 됐었다..

n,t = map(int,input().split())
sub=[[0,0]]
for i in range(n):
    x,y = map(int,input().split())
    sub.append((x,y))
dp=[[0]*(t+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,t+1):
        if j>=sub[i][0]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-sub[i][0]]+sub[i][1])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[n][t])
            
# 코드길이 : 360 B
# 시간 : 644 ms
# 메모리 : 52932 KB
