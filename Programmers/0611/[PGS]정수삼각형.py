def solution(triangle):
    answer = 0
    dp = [0 for _ in range(len(triangle))]
    dp[0] = triangle[0][0]
    return answer
# 풀지 못했다..
# 어떻게 접근해야할지를 몰랐다..
# 근데 막상 다른 사람풀이를 보면 아 이렇게 하면 되겠구나...하고 느끼는 것 같다

# 나는 dp에 많이 약한것같다..ㅠㅠ... => 보완하기...!
# 다른 사람 풀이 참고 : https://school.programmers.co.kr/questions/43193
def solution(triangle):
    dp = [[0 for j in i]for i in triangle]
    dp[0][0] = triangle[0][0]
    a= []
    for i in range(len(triangle)):
        for j in range(i):
            dp[i][j] = max(dp[i][j],dp[i-1][j] + triangle[i][j])
            dp[i][j+1] = dp[i-1][j] + triangle[i][j+1]
    return max(dp[-1])