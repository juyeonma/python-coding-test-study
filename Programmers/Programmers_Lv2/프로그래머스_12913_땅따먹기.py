'''
# 프로그래머스_12913_땅따먹기. Lv 2. 풀이: 23.09.05

# How to
- 동일한 열로 이동 금지
- 점화식
    - i행에서의 최대값 = i-1행에서의 최댓값 + i행의 값
    - 이때, 같은 열은 빼고.
    - dp[i][j] += max(max(dp[i-1][:j]), max(dp[i-1][j+1:]))

# Review
- 풀이 시간: 20분
- 무난한 dp 문제였다.
'''

# Code
# 1. DP: 성공
## 합계: 100.0 / 100.0
## 효율성 테스트 4 〉 통과 (261.49ms, 32.4MB)
def solution(dp):
    n, m = len(dp), len(dp[0])

    for i in range(1, n):
        for j in range(m):
            # 가장자리(j가 0이거나 m-1일 때)는 별도로 처리
            if j == 0:
                dp[i][j] += max(dp[i-1][j+1:])
            elif j == m-1:
                dp[i][j] += max(dp[i-1][:j])
            else: # 0 < j < m-1
                dp[i][j] += max(max(dp[i-1][:j]), max(dp[i-1][j+1:]))
    
    return max(dp[-1])
