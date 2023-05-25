# 이것도 전에 풀었던 문제...

# 진짜.. 어떻게 풀었지?..
# 어떻게 dp가 되는거지,,

# 결국 전에 풀었떤 답을 보았습니다...
# => 참고로 푼 문제들이 기억이 잘 안나는것같다.
# 참고하고 내것으로 만들어야겠다..ㅠㅠ
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        down = i + data[i][j]
        right = j + data[i][j]

        if down < n:
            dp[down][j] += dp[i][j]
        if right < n:
            dp[i][right] += dp[i][j]
print(dp[n-1][n-1])

# 메모리 : 	31256KB 시간: 64ms