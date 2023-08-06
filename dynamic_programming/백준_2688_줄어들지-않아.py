'''
# 백준_2688_줄어들지 않아. 실버 1. 풀이: 23.08.03

# How to
- 오름차순: num[i-1] <= num[i]
- 0으로 시작가능
끝수: 0  1  2  3  4  5  6  7  8  9
n=1: 1  1  1  1  1  1  1  1  1  1
n=2: 1  2  3  4  5  6  7  8  9  10
n=3: 1  3  6  10 15 21 28 36 45 55

- 점화식:
i: 수의 길이, j: 끝 수
dp[i][j] = sum(dp[i-1][:j+1])

# Review
- 풀이 시간: 15분
- 비슷한 유형이 많이 나오는 듯 하다.
'''

# Code
# 1. 성공
## 메모리: 31256 KB, 시간: 48 ms  
import sys
input = sys.stdin.readline()

dp = [[0] * 10 for _ in range(65)]
dp[1] = [1] * 10

for i in range(2, 65):
    for j in range(10):
        # 오름차순이므로, 작거나 같은 수까지만 더하기
        dp[i][j] = sum(dp[i-1][:j+1])
        
for _ in range(int(input())):
    print(sum(dp[int(input())]))