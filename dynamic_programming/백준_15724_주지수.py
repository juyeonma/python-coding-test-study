# DP로 어떻게 풀어야할지 몰라서 참고했다.,.
# 누적합.. -> 범위안에서 누적합을 구하고, 그 전 열들의 합을 뺸다
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
p=[]
for i in range(n):
    p.append(list(map(int,input().split())))

k = int(input())
dp=[[0]*(m) for _ in range(n)]

for j in range(m):
    dp[0][j] = p[0][j]
    
for i in range(1,n):
    for j in range(m):
        dp[i][j]=dp[i-1][j]+p[i][j]
        
# print(dp)

for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    ans = sum(dp[x2-1][y1-1:y2])
    if x1>1:
        ans = ans - sum(dp[x1-2][y1-1:y2])
    print(ans)
    
# 코드길이 : 487 B
# 시간 : 2392 ms
# 메모리 : 80332 KB