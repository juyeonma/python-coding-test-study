'''
# 백준_1915_가장 큰 정사각형. 골드 4. 풀이: 23.07.25

# How to
- 정사각형은 가로세로 변의 길이가 같으니 대각선으로 확인하자.
- dp: 가장 큰 정사각형의 한 변의 길이

## 1. 실패
dp[i][j] = dp[i-1][j-1] + 1
(i행 j-dp[i-1][j-1]:j 열이 모두 0이 아니고, j열 i-dp[i-1][j-1]:i 행이 모두 0이 아닐 때)


## 2. 가로 세로의 연속된 1 개수 구하기: 성공
- 1번 풀이에서 틀린 이유는, 정사각형이 연장되지 않았을 때가 문제였다.
- 무조건 0이 들어있지 않은 경우에만 check를 하다보니, 이전 정사각형이 연장되지는 않지만 그보다 작은 정사각형을 만들 수 있는 경우가 누락됐다.
    - 아래 반례: 1행 1열의 길이 2에서 2행 2열의 길이 3으로 연장되지는 않지만, 새로운 길이 2인 정사각형을 만들 수 있기 때문이다.
- 그래서 현재 좌표를 기준으로 가로 세로로 연속된 1의 길이를 구해 dp를 갱신했다.


## 3. 대각선, 가로, 세로 dp의 최솟값 구하기: 성공
- 2번 풀이는 1의 길이를 매번 구하다보니 pypy에서만 통과된다.
- 직전 행과 열 좌표에 변의 길이가 기록되어 있으므로 매번 1의 개수를 구할 필요가 없다.
    - 즉 변의 길이는 곧 해당 좌표를 중심으로 가로 세로에 연속된 1의 개수를 의미하기 때문.
- 점화식:
dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1


## 반례
원래 배열:
1 1 0
1 1 1
1 1 1

- 2, 3번 코드에서 갱신 후(정답):
1 1 0
1 2 1
1 2 2

- 1번 코드에서 갱신 후(틀림):
1 1 0
1 2 1
1 2 1


# Review
- 풀이 시간: 2시간
- 1번 코드를 작성 후 반례를 만들기까지 꽤 헤맸고, 반례를 출력하고 나서야 2번과 3번 코드로 성공했다.
- 그러나.. 반례를 찾기 까지 너무 오래걸렸다.
- 특히 dp는 반례를 빨리 찾고 문제를 빨리 해결하는게 매우 중요할 것 같다.
'''

# Code
# 1. 실패
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().rstrip())) for _ in range(n)]

def check(i, j):
    # 이번 좌표가 0이거나, 이전 좌표가 0이라면, False
    if dp[i][j] == 0 or dp[i-1][j-1] == 0:
        return False
    
    # 하나라도 0이 있으면, False
    for x in range(i-dp[i-1][j-1], i):
        if dp[x][j] == 0:
            return False

    for y in range(j-dp[i-1][j-1], j):
        if dp[i][y] == 0:
            return False
        
    # 0이 없다면, True
    return True

for i in range(1, n):
    for j in range(1, m):
        # 정사각형이 연장된다면, 변의 길이 + 1
        if check(i, j):
            dp[i][j] = dp[i-1][j-1] + 1

print(max(map(max, dp))**2)


# 2. 가로 세로의 연속된 1 개수 구하기: 성공
## pypy3: 메모리: 124088 KB, 시간: 2432 ms
## python3: 시간초과
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().rstrip())) for _ in range(n)]

# 정사각형의 변의 길이 구하기
def check(i, j):
    # 이번 좌표를 기준으로 가로 세로에 몇개의 1이 연속되는지 구하기
    col = 0
    for x in range(i, i-dp[i-1][j-1]-1, -1):
        if dp[x][j] == 0:
            break
        col += 1

    row = 0
    for y in range(j, j-dp[i-1][j-1]-1, -1):
        if dp[i][y] == 0:
            break
        row += 1
            
    # 이번 좌표의 정사각형의 변의 길이 갱신
    dp[i][j] = min(col, row)
    

for i in range(1, n):
    for j in range(1, m):
        if dp[i][j] == 1 and dp[i-1][j-1] != 0:
            check(i, j)
            
print(max(map(max, dp))**2)


# 3. 대각선, 가로, 세로 dp의 최솟값 구하기: 성공
# 메모리: 56416 KB, 시간: 820 ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().rstrip())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if dp[i][j] == 1:
            # 정사각형의 변의 길이 갱신
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            
print(max(map(max, dp))**2)