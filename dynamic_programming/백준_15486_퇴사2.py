'''
# 백준_15486_퇴사2. 골드 5. 풀이: 23.08.06

# How to
- 선택지는 두가지: i번째 상담을 하거나, 안하거나.
- 상담을 안 한다면, 
    - 직전에 상담 안헀을 때 수익과 현재 수익 중 최댓값
    dp[i][0] = max(dp[i][0], dp[i-1][0])
    
- 인덱스를 벗어나지 않아(i + schedule[i][0] <= n) 상담을 한다면,
    - 상담을 안했을때 수익 + 상담 금액
    dp[i][1] = dp[i][0] + schedule[i][1]
    - 이번 상담이 끝났을 때 날짜도 수익 갱신
    dp[i + schedule[i][0]][0] = max(dp[i + schedule[i][0]][0], dp[i][1])

# Review
- 풀이 시간: 30분
- 인덱스가 조금 헷갈리긴 하는데, 잘 갱신하는게 중요한 문제였다.
- 그런데 이전에 풀어본적이 있는 것 같은 느낌이 든다..?
'''

# Code
# 1. 성공
## 메모리:  KB, 시간:  ms
import sys
input = sys.stdin.readline

n = int(input())
# 기간 t, 금액 p
schedule = [tuple(map(int, input().split())) for _ in range(n)]

# 0: 상담 안함, 1: 상담 함
dp = [[0, 0] for _ in range(n+1)]

for i in range(n):
    # 상담 안한다면, 지나감
    dp[i][0] = max(dp[i][0], dp[i-1][0])
    
    # 상담 한다면,
    if i + schedule[i][0] <= n:
        dp[i][1] = dp[i][0] + schedule[i][1]
        dp[i + schedule[i][0]][0] = max(dp[i + schedule[i][0]][0], dp[i][1])
        
# 최댓값 출력
print(max(map(max, dp)))