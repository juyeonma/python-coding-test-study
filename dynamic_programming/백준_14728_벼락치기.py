'''
# 백준_14728_벼락치기. 골드 5. 풀이: 23.08.03

# How to
- i시간동안 공부를 둘로 쪼개면, i-k과 k 시간. 
    - 즉 i시간 공부했을 때 점수 = i-k시간 공부했을 때 점수 + k시간 공부했을 때 점수
- 현재 단원: k시간 공부해서 s 점수를 얻음.
- i시간을 공부했을 때 최대 점수는,
"기존의 가치 vs i-k시간 공부했을 때의 최대 점수 + 현재 단원을 공부했을 때 점수(=s)"중 더 큰 값
- 점화식: dp[i] = max(dp[i], dp[i-k] + s)

# Review
- 풀이 시간: 30분
- 전에 풀었던 평범한 배낭 문제와 거의 같다.
- 여전히 빠르진 않는데...어디를 최적화 하면 좋을까?
'''

# Code
# 1.
## 메모리: 31256 KB, 시간: 400 ms
import sys
input = sys.stdin.readline

# 단원 개수 n, 공부 가능한 총 시간 t
n, t = map(int, input().split())

# 예상 공부 시간 k, 배점 s
arr = [list(map(int, input().split())) for _ in range(n)]
    
# i시간 공부했을 때 최대 점수
dp = [0] * (t+1)

for k, s in arr:
    # 현재 단원의 공부 시간 이상의 최대 점수 탐색
    for i in range(t, k-1, -1):
        dp[i] = max(dp[i], dp[i-k] + s)
        
print(dp[t])