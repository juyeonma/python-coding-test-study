t = int(input())
for _ in range(t):
    n = int(input())
    coin=list(map(int,input().split()))
    m = int(input())
    
    dp=[0]*(m+1)
    dp[0]=1
    
    #2차원 배열로 문제를 이해했을 때, 
    #dp[i]에는 현재 i값에 현재 계산된 coin의 값을 뺀 값의 경우의 수의 합과 같다..
    for c in coin:
        for i in range(1,m+1):
            if i>=c:
                dp[i]=dp[i]+dp[i-c]
    print(dp[m])
    
# 코드길이 : 275 B
# 시간 : 80 ms
# 메모리 : 31256 KB