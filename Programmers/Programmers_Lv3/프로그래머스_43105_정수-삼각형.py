'''
# 프로그래머스_43105_정수 삼각형. Lv 3. 풀이: 23.06.09

# How to
- 아래로 갈 수록 index가 늘어나기 때문에, n-1행을 구하려면 index 범위값을 나누어야함.
- 점화식:
    - 0행을 구하려면: dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + dp[i][j]
    - n-1행을 구하려면: dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
- Top-Down도 같은 로직
    - 다만 dp[i][j]를 구할때 앞에는 재귀호출로, 뒤에는 triangle[i][j]로 하면 된다.
    - 또한 Bottom-Up은 입력을 그대로 dp로 썼지만, Top-Down은 별도로 dp 만들어야함.

- 따라서, Bottom-Up으로 n-2행부터 거꾸로, 0행에서 수렴하는게 제일 빠르고 간단하다.
    
# Review
- 전형적인 dp문제. 다만 0행으로 수렴할지, n-1행으로 수렴할지 조금 고민했다.
'''


# 1. Bottom-Up Code: 성공
# 1-1. 0행 구하기: n-2행부터 거꾸로 구함
## 효율성 테스트 6 〉통과 (46.23ms, 14.6MB)
def solution(dp):
    for i in range(len(dp)-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + dp[i][j]

    return max(dp[0])


# 1-2. n-1행 구하기: 2행부터 순차적으로 구함
## 효율성 테스트 6 〉통과 (50.56ms, 14.8MB)
def solution(dp):
    for i in range(1, len(dp)):
        for j in range(i+1):
            if 0 < j < i: # 직전행의 오른쪽과 왼쪽 중 큰값에 더함.
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
            elif j == 0: # 직전 행의 오른쪽에 더함
                dp[i][j] = dp[i-1][j] + dp[i][j]
            else: # j == i. 직전 행의 왼쪽에 더함
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
                
    return max(dp[-1])


# 2. Top-Down Code: 성공
# 2-1. 0행 구하기
## 효율성 테스트 6 〉통과 (68.48ms, 19.6MB)
def make_dp(i, j, dp, t):
    if dp[i][j]:
        return dp[i][j]

    dp[i][j] = max(make_dp(i+1, j, dp, t), make_dp(i+1, j+1, dp, t)) + t[i][j]

    return dp[i][j]

def solution(triangle):
    n = len(triangle)
    dp = [[0] * (i+1) for i in range(n)]
    dp[-1] = triangle[-1]
    answer = 0
    answer = max(answer, make_dp(0, 0, dp, triangle))

    return answer


# 2-2. n-1행 구하기
## 효율성 테스트 6 〉통과 (77.88ms, 19.2MB)
def make_dp(i, j, dp, t):
    if dp[i][j]:
        return dp[i][j]
    
    if 0 < j < i: # 직전행의 오른쪽과 왼쪽 중 큰값에 더함
        dp[i][j] = max(make_dp(i-1, j-1, dp, t), make_dp(i-1, j, dp, t)) + t[i][j]
        
    elif j == 0: # 직전 행의 오른쪽에 더함
        dp[i][j] = make_dp(i-1, j, dp, t) + t[i][j]
        
    else: # j == i. 직전 행의 왼쪽에 더함
        dp[i][j] = make_dp(i-1, j-1, dp, t) + t[i][j]

    return dp[i][j]

def solution(triangle):
    n = len(triangle)
    dp = [[0] * (i+1) for i in range(n)]
    dp[0] = triangle[0]
    answer = 0
    for j in range(n):
        answer = max(answer, make_dp(n-1, j, dp, triangle))

    return answer


# 다른 사람 풀이
## 1. lambda를 이용한 숏코딩
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])


'''
# Result
풀이 시간: 20분
효율성 테스트 6 〉통과 (46.23ms, 14.6MB)
'''