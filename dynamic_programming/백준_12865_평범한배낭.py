#냅색 알고리즘
n,k  = map(int,input().split())
bag = [[0,0]]
for _ in range(n):
    bag.append(list(map(int,input().split())))

dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w = bag[i][0] #물건 무게
        v = bag[i][1] #물건 가치
        
        if j<w: #현재 물건이 지금까지 무게보다 크다면
            dp[i][j]=dp[i-1][j] #그 전 물건들의 가치를 그대로 갖고 옴
        else:
            dp[i][j]=max(v+dp[i-1][j-w], dp[i-1][j]) #현재 물건의 가치를 더했을 때, 이전의 가치보다 큰지 작은지 판단
print(dp[n][k]) #마지막에 저장된 값을 출력

# 코드길이 : 647 B
# 시간 : 5892 ms
# 메모리 : 282468 KB