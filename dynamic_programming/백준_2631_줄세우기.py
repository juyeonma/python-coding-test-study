'''
# 백준_2631_줄세우기. 골드 4 풀이: 23.07.29

# How to
## 예제
배열: 3 7 5 2 6 1 4
dp: 1 2 2 1 3 1 2

- dp: 해당 인덱스까지 최대 증가 수열의 길이
- 점화식: 
    - j번째 값 < i번째 값이 라면,
    - dp[i] = max(dp[i], dp[j]+1)

# Review
- 풀이 시간: 1시간
- 전에 풀었던 전깃줄 문제와 비슷한데, 최대 증가 수열의 길이를 구현하는데 조금 헤맸다.
'''

# Code
# 1. 성공
## 메모리: 31256 KB, 시간: 48 ms
import sys
input = sys.stdin.readline

n = int(input())
children = [int(input()) for _ in range(n)]
# 수열의 길이가 1일때는 증가하는 길이도 1이므로, 1로 초기화
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if children[j] < children[i]:
            dp[i]= max(dp[i], dp[j]+1)

# 증가하지 않는 부분만 이동하면 됨
print(n - max(dp))