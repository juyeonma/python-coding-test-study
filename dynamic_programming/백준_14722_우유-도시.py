'''
# 백준_14722_우유 도시. 골드 4. 풀이: 23.05.28 -> 실패

# How to
- 딸기 -> 초코 -> 바나나
- Top-Down 방식으로, 이전 갯수 +1 갱신하기

## 반례
- 0, 0이 0(딸기우유)가 아닌경우
3
2 2 1
2 1 1
1 1 0
답: 1

# Review
- 0, 0의 위치가 0이 아닐때를 어떻게 해야할지 모르겠다.
    - 즉, dp[0][0]이 0이면, 재귀 깊이가 깊어져서 시간초과가 나는 듯 하다.
'''

# 실패 Code
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 우유도시: n*n
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
if arr[0][0] == 0:
    dp[0][0] = 1

def solve(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return 0
    
    # 딸기 0 -> 초코 1 -> 바나나 2
    # 차이는 1 or -2
    a, b = 0, 0
    if arr[x][y] - arr[x-1][y] in (1, -2):
        a = 1
        
    if arr[x][y] - arr[x][y-1] in (1, -2):
        b = 1
    
    # 우유 갯수 갱신
    dp[x][y] = max(solve(x-1, y)+a, solve(x, y-1)+b)
    
    return dp[x][y]

print(solve(n-1, n-1))


# Bottom-Up
# for x in range(n-1):
#     for y in range(n-1):
#         a, b = 0, 0
#         if arr[x+1][y] - arr[x][y] in (1, -2):
#             a = 1
#         if arr[x][y+1] - arr[x][y] in (1, -2):
#             b = 1

#         dp[x][y] = 



'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''