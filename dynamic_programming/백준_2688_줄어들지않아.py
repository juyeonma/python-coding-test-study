#런타임에러
t = int(input())
dp=[[1]*10 for _ in range(65)]

for j in range(10):
    dp[1][j]=1

for i in range(2,65):
    for j in range(9):
        dp[i][j]=sum(dp[i-1][j:])
print(dp[:4])       
for _ in range(t):
    n = int(input())
    print(sum(dp[n]))

# 어떻게 해야 런타임에러가 안날까..    
# t = int(input())
  
# for _ in range(t):
#     n = int(input())
    
#     dp=[[1]*10 for _ in range(n+1)]

#     for j in range(10):
#         dp[2][j]=10-j

#     for i in range(2,n+1):
#         for j in range(9):
#             dp[i][j]=sum(dp[i-1][j:])
            
#     print(sum(dp[n]))

# 코드길이 : 231 B
# 시간 : 48 ms
# 메모리 : 31256 KB