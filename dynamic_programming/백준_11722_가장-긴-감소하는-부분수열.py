'''
# 백준_11722_가장 긴 감소하는 부분수열. 실버 2. 풀이: 23.05.18

# How to
- 점화식
각 숫자의 최소 수열 길이는 1
j: i보다 작은 인덱스
모든 수를 탐색하며 최댓값 갱신
dp[i] = max(dp[i], dp[j]+1)

# Review
- 코드는 간단하지만, 부분수열을 중복으로 탐색하게 되니까 시간이 은근히 많이 걸린다.
- 탑다운 방식으로 어떻게 구현할 수 있을까? 결국 모든 인덱스의 수와 비교해야할텐데..
'''

# Bottom-up Code
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] < nums[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

'''
# Result
풀이 시간: 20분
메모리: 31256 KB
시간: 168 ms
코드 길이: 238 B
'''