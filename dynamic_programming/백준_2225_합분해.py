'''
# 백준_2225_합분해. 골드 5. 풀이: 23.07.28 -> 실패

# How to
## 1. 실패
- k=1 일 때, dp[i][1] = 1
- k=2 일 때, dp[i][2] = i+1
- 탑다운?

# Review
- 풀이 시간:
- 점화식을 어떻게 세워야할지 감이 잡히지 않는다. 탑다운인지, 바텀업인지도 잘 모르겠다.. 이게 골드 5라고?
'''

# Code
# 1. 실패
## 메모리:  KB, 시간:  ms
n, k = map(int, input().split())
    
dp = [i for i in range(1, n+2)]
dp = [[0] * (k+1) for _ in range(n+1)]

def solve(num, cnt):
    if num < 0 or cnt < 0:
        return 
    
    if cnt == 1:
        dp[num][1] = 1
        return 1
    
    elif cnt == 2:
        dp[num][2] = num+1
        return num+1
    
    tmp = 0
    for i in range(num):
        dp[i][1] = solve(i, 1)
        dp[num-i][cnt-1] = solve(num-i, cnt-1)
        tmp += dp[i][1] + dp[num-i][cnt-1]

    dp[num][cnt] = tmp
    return dp[num][cnt]

solve(n, k)
print(dp[-1][-1])

