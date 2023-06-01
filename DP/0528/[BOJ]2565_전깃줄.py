# 가장 긴 증가하는 부분 수열과 연관있는 문제라고 한다..
# 가장 긴 감소하는 부분 수열 풀었는데 생각하지 못하다니ㅜㅜ..
# 참고 : https://hongcoding.tistory.com/157
import sys
input = sys.stdin.readline

data = []
n = int(input())
dp = [1] * n
for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b])

data.sort()

for i in range(1, n):
    for j in range(0, i):
        if data[j][1] < data[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))