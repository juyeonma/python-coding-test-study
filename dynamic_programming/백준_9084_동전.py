'''
# 백준_9084_동전. 골드 5. 풀이: 23.07.25

# How to
- 0원을 만들기 위한 경우의 수는 1
dp[0] = 1
- 만약 현재 i원이 있다면, n원을 만드는 경우의 수 = 기존 n원을 만드는 경우의 수 + i원을 만드는 경우의 수
dp[n] = dp[n] + dp[n-i]

## 예제
동전: 2, 3
i = 2
dp[2] = dp[2] + dp[2-2] = 0 + 1 = 1
dp[3] = dp[3] + dp[3-2] = 0 + 0 = 0
dp[4] = dp[4] + dp[4-2] = 0 + 1 = 1
dp[5] = dp[5] + dp[5-2] = 0 + 0 = 0
dp[6] = dp[6] + dp[6-2] = 0 + 1 = 1

i = 3
dp[3] = dp[3] + dp[3-3] = 0 + 1 = 1
dp[4] = dp[4] + dp[4-3] = 1 + 0 = 1
dp[5] = dp[5] + dp[5-3] = 0 + 1 = 1
dp[6] = dp[6] + dp[6-3] = 1 + 1 = 2


# Review
- 풀이 시간: 30분
- 전에 백준에서 푼 문제와 같았다.
- 그러나.. 자꾸만 이런 류의 동전 문제에서 헤매곤 한다. 
    - 첫번째 반복문은 동전으로, 두번째 반복문은 금액으로 설정해야함을 잊지말자.
'''

# Code
# 1.
## 메모리: 31256 KB, 시간: 56 ms
import sys
input = sys.stdin.readline

def solve():
    _ = int(input())
    coin = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target+1)
    dp[0] = 1
    
    for i in coin:
        for j in range(i, target+1):
            dp[j] += dp[j-i]
    
    return dp[-1]

for _ in range(int(input())):
    print(solve())
    