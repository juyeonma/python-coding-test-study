'''
# 프로그래머스_42898_등굣길. Lv 3. 풀이: 23.06.25

# How to
- 점화식: dp[i][j] = dp[i-1][j] + dp[i][j-1]
    - i, j까지 최단경로의 수 = i-1, j까지 최단경로의 수 + i, j-1까지 최단경로의 수
        
## 반례

# Review
- 처음에 '최단경로의 개수'가 아니라 '최단경로'를 묻는 줄 알고 헛수고를 했다..
'''

# 1. Top-Down: 성공
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    puddles_set = set([tuple(i) for i in puddles])

    def solve_dp(i, j):
        # 웅덩이이거나, 지도를 벗어날 경우, 0 return
        # 웅덩이 좌표: 문제에서 col, row 순서로 되어있음
        if (j+1, i+1) in puddles_set or i < 0 or i >= n or j < 0 or j >= m:
            return 0
        
        if dp[i][j]:
            return dp[i][j]

        # i, j까지 최단경로의 수 = i-1, j까지 최단경로의 수 + i, j-1까지 최단경로의 수
        dp[i][j] = (solve_dp(i-1, j) + solve_dp(i, j-1)) % 1_000_000_007

        return dp[i][j]
    
    return solve_dp(n-1, m-1) 


# 그외: '최단경로'를 구하느라 헛수고한 Code
# 점화식: dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    puddles_set = set([tuple(i) for i in puddles])

    def solve_dp(i, j):
        if (j+1, i+1) in puddles_set or i < 0 or i >= n or j < 0 or j >= m:
            return 200
        
        if dp[i][j]:
            return dp[i][j]

        dp[i][j] = (min(solve_dp(i-1, j), solve_dp(i, j-1)) + 1) % 1_000_000_007

        return dp[i][j]

    return solve_dp(n-1, m-1) - 1


'''
# Result
풀이 시간: 30분
테스트 1 〉	통과 (5.85ms, 10.3MB)
'''