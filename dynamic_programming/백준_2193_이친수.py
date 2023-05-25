'''
# 백준_2193_이친수. 실버 3. 풀이: 23.05.22

# How to
- 이친수?
    - 0으로 시작하지 않는다.
    - 1은 연속되지 않는다.
    
- 점화식
1, 1, 2, 3, 5, 8 => 피보나치 수열과 같다!
dp[n] = dp[n-1] + dp[n-2]
dp[1], dp[2] = 1, 1


# Review
- 처음에는 이진법으로 생각했다. 즉 2^(n-1) 수중에서 1이 연속으로 없는 횟수를 세도록.
- 계단 밟기 문제와 유사하다고도 생각했다.
    - 마지막 계단은 무조건 밟아야함 == 첫번째는 무조건 1로 시작
    - 계단을 연속으로 밟을 수 없음 == 1은 연속되지 않는다.
- 우선 1부터 차례대로 답을 적어보니, 익숙한 피보나치 수열을 발견했다. 그래서 바로 구현 끝
'''

# 1. Top-Down Code
n = int(input())
dp = {1: 1, 2: 1}

def solve(n):
    if n in dp:
        return dp[n]
    # n = (n-1) + (n-2)
    dp[n] = solve(n-1) + solve(n-2)
    return dp[n]
    
print(solve(n))

# 2. Bottom-Up Code
n = int(input())
# n-2, n-1
a, b = 1, 1

# a가 첫번째, b가 두번째. 그래서 3번째 수부터 시작
for _ in range(3, n+1):
    # 한칸 전진함에 따라 n-1이 n-2가 되고, (n-1)+(n-2), 즉 n이 새로운 n-1이 된다.
    a, b = b, a + b

print(b)

'''
# Result
풀이 시간: 20분
메모리: 31256 KB
시간: 40 ms
코드 길이: 160 B
'''