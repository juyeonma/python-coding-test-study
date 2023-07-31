n,m=map(int,input().split())
num = []
for _ in range(n):
    num.append(list(map(int,list(input()))))
    
dp=[[0]*(m+1) for _ in range(n+1)]
ans =0
# 현재 탐색을 기준으로 왼쪽 대각석 위의 값이 1이면 정사각형이 만들어질 수 있기 때문에
# 그때의 현재 위치에서 주변 값들의 최솟값을 구해서 1을 더한다.
for i in range(1,n+1):
    for j in range(1,m+1):
        if num[i-1][j-1]==1:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        ans=max(ans,dp[i][j])

print(ans*ans)

# 코드길이 : 336 B
# 시간 : 1072 ms
# 메모리 : 64296 KB