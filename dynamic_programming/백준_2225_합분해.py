n,k = map(int,input().split())
dp = [[0]*201 for _ in range(201)]

#k가 2일 경우일 까지 미리 담아주어야 다음 계산에서 오류가 안남
for i in range(201):
    dp[1][i]=1
    dp[2][i]=i+1

# 2차원 표로 그려봤을 때 현재 위치의 왼쪽과 위의 값을 합한 값이 현재 위치의 합이다.
for i in range(2,201):
    dp[i][1]=i
    for j in range(2,201):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]
        
print(dp[k][n]%1000000000)

# 코드길이 : 260 B
# 시간 : 60 ms
# 메모리 : 33300 KB