#시간초과 때문에 시간이 걸렸다 ㅜ
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

dp=[1]*(n+1)
sub=[]
for i in range(m):
    x,y = map(int, input().split())
    sub.append((x,y))
sub.sort()
for i,j in sub:
    if dp[i]>=dp[j]:
        dp[j]=dp[i]+1

# for i in range(1,n+1):
#     print(dp[i], end=' ')
print(*dp[1:])
    
# 코드길이 : 305 B
# 시간 : 1376 ms
# 메모리 : 93548 KB
