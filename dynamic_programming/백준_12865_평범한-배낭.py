'''
# 백준_12865_평범한 배낭. 골드 5. 풀이: 23.07.27

# How to
## 2.
- arr: 무게 i의 가치
- dp: 무게 i까지의 최대 가치
dp[n] = max(dp[n], dp[n-i] + arr[i])
- n = a + b 라고 할 때,
- 무게 n까지 최대 가치는 곧 기존의 가치와 무게 b까지 최대 가치 + 무게 a에서의 가치 중 최댓값

# Review
- 풀이 시간: 30분
- 역시 dfs로 조합을 구현한 풀이는 시간초과가 떴고, 결국 dp로 풀었다.
- 그런데 dp에서 시간이 매우 오래 걸렸는데, dp를 길이 k의 리스트로 하다보니 빈 부분이 많아서 그런 것 같다.
    - 딕셔너리로 하면 더 빠를거 같으니 다시 해봐야겠다.
'''

# Code
# 1. dfs 풀기: 실패
## 메모리:  KB, 시간:  ms
import sys
input = sys.stdin.readline

# 물품 수 n, 최대 무게 k
n, k = map(int, input().split())

# 무게 w, 가치 v
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
answer = 0
def combination(idx, w, v):
    global answer
    if w > k:
        return
    
    if idx == n:
        answer = max(answer, v)
        return
    
    for i in range(idx+1, n):
        if not visited[i]:
            visited[i] = True
            combination(i, w+arr[i][0], v+arr[i][1])
            visited[i] = False
            
    combination(idx+1, w, v)
    
combination(-1, 0, 0)
print(answer)


# 2. DP로 풀기: 성공 -> 딕셔너리로 다시 풀어보기
## 메모리: 35108 KB, 시간: 3376 ms
import sys
input = sys.stdin.readline

# 물품 수 n, 최대 무게 k
n, k = map(int, input().split())

# 무게 w, 가치 v
arr = [list(map(int, input().split())) for _ in range(n)]

# 인덱스: 무게, 값: 최대 가치
dp = [0] * (k+1)

for i, (w, v) in enumerate(arr):
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)
        
# 무게 k까지의 최대 가치는?
print(dp[k])