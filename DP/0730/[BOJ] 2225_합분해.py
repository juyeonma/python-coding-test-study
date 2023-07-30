# DP로 안 풀고.. 다른 방식으로 풀어버렸다... => 수학 방식으로 접근한듯..
# 계산할려고 보니깐 중복 조합인가 싶어서 식을 찾아보았다..
# 중복 조합 식을 이용
# - n+r-1 C r
# 근데 중복 조합 식은 아닌 것 같다..

n, k = map(int, input().split())
# 근데 k는 r이 아닌 k-1이 r이어야 정답이 됨..
# 왜..일까... 1은 답이 하나로 정해져서 그런건가?..흠..
if k == 1:
    print(1)
else:
    # 즉..
    # 중복 조합 식을 응용해서
    # n+r-1 C r-1 => 이렇게 해야 정답이 됨..
    s = n+k-1
    r = k - 1
    sum = 1
    cnt = 1
    for i in range(r):
        sum *= s
        s -= 1
        cnt *= r
        r -= 1
    result = sum//cnt
    print(result % 1000000000)

# DP 풀이 방식
# 참고 : https://computer-choco.tistory.com/545
# 막상보니..쉽다...
N, K = map(int, input().split())

dp = [[1 for i in range(N+1)] for j in range(K+1)]

for i in range(2,K+1):
    for j in range(1,N+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[K][N])