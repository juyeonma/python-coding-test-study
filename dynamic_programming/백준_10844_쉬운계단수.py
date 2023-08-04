n = int(input())
dp = [[0]*10 for _ in range(101)]
for i in range(1,10):
    dp[1][i]=1

# 점화식을 어떻게 세워야할 지 모르겠다,,ㅜ
for i in range(2,101):
    for j in range(10):
        if j==0:
            dp[i][j]
    
print(dp[n]%1000000000)

# 코드길이 : 302 B
# 시간 :  ms
# 메모리 :  KB
