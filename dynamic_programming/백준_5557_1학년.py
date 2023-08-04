# 모르겠다..
n = int(input())
num = list(map(int,input().split()))

dp=[[0]*21 for _ in range(n)]

dp[0][num[0]]=1 #첫번째 문자는 무조건 더해야한다

# 마지막 두 숫자는 값을 더하지 않으니까 n-1까지로 범위를 제한 둔것 같다

for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]: #전에 계산을 했던 행일 경우,,
            if j+num[i]<=20:
                dp[i][j+num[i]]+=dp[i-1][j]
            if j-num[i]>=0:
                dp[i][j-num[i]]+=dp[i-1][j]

print(dp[n-2][num[n-1]]) #이부분도 잘 모르겠다