'''
# 백준_17175_피보나치는 지겨웡~. 실버 3. 풀이: 23.05.22

# How to
- 호출 횟수도 피보나치 수열과 비슷함.
- 점화식: dp[n] = dp[n-2] + dp[n-1] + 1

n:
0, 1, 2, 3, 4, 5, 6..

피보나치 수열:
0, 1, 1, 2, 3, 5, 8..

호출 횟수: 
1, 1, 3, 5, 9, 15, 25..


# Review
- 처음에는 문제에서 제시된 함수에서 전역변수로 호출횟수를 셌는데, 시간초과가 떴다.
- 다시 생각해보니, 어짜피 호출횟수가 필요한거니까 굳이 피보나치 수열을 기록할 필요가 없었다.
- 그래서 호출횟수의 점화식을 만들고, bottom-up 방식으로 성공!
'''

# 1. 69% 시간초과 Code
dp = {0: 0, 1: 1}
answer = 0

def fibonacci(n):
    global answer
    answer += 1
    if n < 2:
        return n
    dp[n] = fibonacci(n-2) + fibonacci(n-1)
    return dp[n]

tmp = fibonacci(int(input()))
print(answer % 1_000_000_007)

# # 굳이 dp에 저장할 필요가 없네

# 2. 성공 Code
n = int(input())
dp = [0] * (n+1)
dp[0] = 1
if n > 0:
    dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1] + 1

print(dp[n] % 1_000_000_007)


'''
# Result
풀이 시간: 20분
메모리: 31256 KB
시간: 48 ms
코드 길이: 156 B
'''