'''
# 백준_2636_치즈. 골드 4. 풀이: 23.05.28 -> 실패

# How to
- 흑과 백은 각각 15명으로 한정되어 있으므로, 이중 for문으로 입력시마다 탐색
- 점화식
dp[a][b] : 백은 a명, 흑은 b명일 때의 능력치
dp[a][b] = max(dp[a][b], dp[a-1][b]+white, dp[a][b-1]+black)

# Review
- 왜 실패일까..진짜 왜 틀렸을까..도저히 모르겠다ㅠㅠ
'''

# 1. Top-Down 실패
import sys
input = sys.stdin.readline

answer = 0
dp = [[0] * 16 for _ in range(16)]
# 첫줄은 우선 포함해서? -> 이 줄을 포함해야할까?
dp[1][0], dp[0][1] = map(int, input().split())

def solve(a, b):
    global white, black    
    if dp[a][b]:
        return dp[a][b]
    
    # 이번 선수 포함X vs 백팀 O vs 흑팀 O
    if a >= 1 and b >= 1:
        dp[a][b] = max(dp[a][b], solve(a-1, b)+white, solve(a, b-1)+black)
        
    # 이번 선수 포함X vs 백팀 O
    elif a >= 1:
        dp[a][b] = max(dp[a][b], solve(a-1, b)+white)
        
    # 이번 선수 포함X vs 흑팀 O
    elif b >= 1:
        dp[a][b] = max(dp[a][b], solve(a, b-1)+black)
        
    return dp[a][b]


while True:
    try:
        white, black = map(int, input().split())
        # 최댓값 구하기
        answer = max(answer, solve(15, 15))
        
    except:
        print(answer)
        break
    

# 2. Bottom-Up 실패
import sys
input = sys.stdin.readline

answer = 0
dp = [[0] * 16 for _ in range(16)]
while True:
    try:
        white, black = map(int, input().split())
        # 0명부터 차근차근 쌓아가기
        for a in range(16):
            for b in range(16):
                # 이번 선수 포함X vs 백팀 O vs 흑팀 O
                if a >= 1:
                    dp[a][b] = max(dp[a][b], dp[a-1][b]+white)
                
                if b >= 1:
                    dp[a][b] = max(dp[a][b], dp[a][b-1]+black)
           
    except:
        print(dp[15][15])
        break

'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''