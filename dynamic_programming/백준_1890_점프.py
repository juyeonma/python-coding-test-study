'''
# 백준_1890_점프. 실버. 풀이: 23.05.24

# How to
- 거꾸로 생각해서 점프 가능 여부를 따진 다음에, 경우의 수를 누적

result: a, b에서 x, y로 점프 가능할 때, 경우의 수
- 같은 행일때, 점프 가능하면(abs(b-y) == arr[x][b])
    result += dp[x][b]
- 같은 열일때, 점프 가능하면(abx(a-x) == arr[a][y])
    result += dp[a][y]
    

# Review
- dp는 정말 난이도 차이가 엄청난게, 점화식만 바로 생각나면 금방 풀린다..
'''

# Code
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 경우의 수가 0일수도 있으므로, 초기값을 -1로 세팅해둠
dp = [[-1]*n for _ in range(n)]
# 0행 또는 0열일 때는 0, 0 에서의 값만큼 점프할 때, 경우의 수 = 1
dp[0][arr[0][0]], dp[arr[0][0]][0] = 1, 1

def solve(x, y):
    # 범위 밖이면, 경우의 수는 0
    if x < 0 or y < 0 or x >= n or y >= n:
        return 0
    # 이미 점프해봤다면, 경우의 수 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    result = 0
    # 같은 행일때, 점프 가능하면
    for i in range(y):
        if abs(i-y) == arr[x][i]:
            result += solve(x, i)
            
    # 같은 열일때, 점프 가능하면
    for i in range(x):
        if abs(i-x) == arr[i][y]:
            result += solve(i, y)
    dp[x][y] = result
    return result

print(solve(n-1, n-1))


'''
# Result
풀이 시간: 20분
메모리: 31256 KB
시간: 44 ms
코드 길이: 592 B
'''