'''
# 백준_2579_계단 오르기. 실버 3. 풀이: 23.05.17

# How to
- 점화식
0: 한 계단 밟고 올라옴: n-3 -> n-1 -> n 밟음
dp[n][0] = dp[n-1][1] + step[n]

1: 두 계단 밟고 올라옴: n-2 -> n 밟음
dp[n][1] = max(dp[n-2][0], dp[n-2][1]) + step[n]

# Review
- 점화식은 바로 세울 수 있어서 쉬웠다. 예전에 징검다리 문제와 유사하다.
- 다 풀고나서 sys 여부나, max 값을 dp에서 넣을건지 출력할때 할건지, 탑다운 등 실험을 해보니까 딱히 차이가 나지 않았다.
'''

# Bottom-up Code
## 1번: 직전에 한칸씩과 두칸씩 이동으로 나누어서 저장
## 31256 KB, 52 ms -> sys 하니까: 31256 KB, 40 ms
import sys
input = sys.stdin.readline

n = int(input())
step = [int(input()) for _ in range(n)]
dp = [[0, 0] for _ in range(n)]
dp[0][0], dp[0][1] = step[0], step[0]
if n > 1:
    dp[1][0], dp[1][1] = step[0]+step[1], step[1] 

for i in range(2, n):
    dp[i][0] = dp[i-1][1] + step[i]
    dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + step[i]
    
print(max(dp[n-1][0], dp[n-1][1]))


## 2번: dp를 구할때, 바로 max값을 넣어볼까?
## 31256 KB, 40	ms
import sys
input = sys.stdin.readline

n = int(input())
step = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = step[0]
if n > 1:
    dp[1] = step[0]+step[1]

# 사실 dp[2]까지 미리 입력해놓고, for문에서 3부터 탐색하는게 맞긴 하지만
# i가 2일때, dp[-1]은 0이므로 코드는 돌아가긴 함..
for i in range(2, n):
    dp[i] = max(dp[i-3]+step[i-1], dp[i-2]) + step[i]
    
print(dp[n-1])


# Top-down Code
## 3번: 탑다운으로 작성하면?
## 31256 KB, 40	ms
import sys
input = sys.stdin.readline

n = int(input())
step = [int(input()) for _ in range(n)]
# solve(-1)이 나올수 있어서, -1을 key로 넣어줌
dp = {-1: 0, 0: step[0]}
if n > 1:
    dp[1] = step[0]+step[1]
    
def solve(n):
    if n in dp:
        return dp[n]
    
    dp[n] = max(solve(n-3)+step[n-1], solve(n-2)) + step[n]
    return dp[n]
    
print(solve(n-1))


'''
# Result
풀이 시간: 20분
메모리: 31256 KB
시간: 40 ms
코드 길이: 319 B
'''