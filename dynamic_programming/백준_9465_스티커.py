'''
# 백준_9465_스티커. 실버 1. 풀이: 23.05.25 -> 실패

# How to
1. 위, 왼쪽, 왼쪽 대각선의 dp로 최댓값 구하기 -> 실패
- i, j번째의 최대 점수 = i, j번째를 붙이거나 안 붙이는 것 점수 중 최댓값
dp[i][j] = max(dp[i-1][j-1] + sticker[i][j], max(dp[i-1][j], dp[i][j-1]))

- 실패 이유
    - sticker[i+1][j-1] 가 누락됨
    - 예: 예제1-1에서 dp[1][2]는 200이어야 하는데, 150으로 나옴.


2. 위, 왼쪽, 왼쪽 아래의 dp로 최댓값 구하기 -> 실패
a: i, j번째를 붙인다면
b: i, j번째를 안 붙인다면
c: i, j번째의 최대 점수

a = max(dp[i-1][j][0], dp[i][j-1][0], dp[i+1][j-1][1]) + sticker[i][j]
b = max(dp[i-1][j][1], dp[i][j-1][1], dp[i+1][j-1][1])
dp[i][j] = [b, max(a, b)]


3. 결국 구글링: 전 열의 대각선, 전전 열의 대각선 중 큰 값 + 현재 점수 -> 성공
j열의 최대 점수 = max(dp[0][j], dp[1][j])
dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + dp[0][j]
dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + dp[1][j]


# Review
- 진짜..진짜 너무 시간을 많이 썼는데, 구글링 하고 나서 허무했다. 이걸 고려 못하다니..?
    - 0과 1행을 나누어 각각 스티커를 붙인다고 가정하고 대각선을 살펴야했다.
        - 어짜피 위에 스티커를 붙이면 아래는 붙일 수 없기 때문이다.
- 실패했던 이유는, 스티커를 붙이거나 안 붙이는 경우를 고려했기 때문이다. 
    - 그렇게 하면 스티커를 붙이지 않았을때, 다음행의 대각선 값이 자꾸 누락되는 문제가 생겼다.
- 행과 열이 존재하는 경우의 dp는 대각선을 고려해야한다는 것을 깨달았다.
- dp 진짜 너무 너무 어렵다.. 고작 실버에 이렇게 시간을 쏟고도 점화식을 구하지 못하다니.
'''

# 3. 구글링으로 아이디어! -> 성공
# 3-1. dp에 저장하기: 47876 KB 760 ms	
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    if n >= 2:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

    for j in range(2, n):
        dp[0][j] += max(dp[1][j-1], dp[1][j-2])
        dp[1][j] += max(dp[0][j-1], dp[0][j-2])
        
    # j열의 최대 점수 = max(dp[0][j], dp[1][j])
    print(max(dp[0][n-1], dp[1][n-1]))
    
    
# 3-2. 매번 전 대각선과 전전 대각선 갱신하기: 39300 KB 528 ms	
# 함수로 따로 안 빼면? 41468 KB 692 ms
import sys
input = sys.stdin.readline

# 함수로 만들어서 조금 더 빨라진것!
def solve(n):
    dp = [list(map(int, input().split())) for _ in range(2)]

    a2, a1 = 0, dp[0][0]
    b2, b1 = 0, dp[1][0]

    for j in range(1, n):
        # 전 대각선이 전전 대각선이 되고, 새로 계산한 값이 전 대각선이 된다.
        a2, a1, b2, b1 = a1, max(b2, b1)+dp[0][j], b1, max(a2, a1)+dp[1][j]
    
    # j열의 최대 점수 = max(dp[0][j], dp[1][j])
    return max(a1, b1)
    
for _ in range(int(input())):
    print(solve(int(input())))
    

# 2. 위, 왼쪽, 왼쪽 아래 -> 실패
def solve(i, j):
    if i < 0 or j < 0 or i >= 2 or j >= n:
        return [0, 0]
    if dp[i][j] != [-1, -1]:
        return dp[i][j]
    x, y, z = solve(i-1, j), solve(i, j-1), solve(i+1, j-1)[1]
    a, b = max(x[0], y[0], z) + sticker[i][j], max(x[1], y[1], z)
    dp[i][j] = [b, max(a, b)]
    return dp[i][j]

for _ in range(int(input())):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[[-1]*2 for _ in range(n)] for _ in range(2)]
    dp[0][0] = [0, sticker[0][0]]
    dp[1][0] = [sticker[0][0], max(sticker[0][0], sticker[1][0])]
    if n > 1:
        dp[0][1] = [sticker[0][0], max(sticker[0][0], sticker[0][1])]
    print(solve(1, n-1)[1])


# 1. 위, 왼쪽, 왼쪽 대각선 -> 실패
def solve(i, j, dp, sticker):
    if dp[i][j] >= 0:
        return dp[i][j]
    if i == 0:
        dp[i][j] = max(solve(i, j-2, dp, sticker) + sticker[i][j], solve(i, j-1, dp, sticker))
    else:
        dp[i][j] = max(solve(i-1, j-1, dp, sticker) + sticker[i][j], max(solve(i-1, j, dp, sticker), solve(i, j-1, dp, sticker)))
    return dp[i][j]
    
for _ in range(int(input())):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = max(sticker[0][0], sticker[1][0])
    if n > 1:
        dp[0][1] = max(sticker[0][0], sticker[0][1])
    print(solve(1, n-1, dp, sticker))    
    
    
'''
# Result
풀이 시간: 실패
메모리: 39300 KB
시간: 528 ms
코드 길이: 365 B
'''	