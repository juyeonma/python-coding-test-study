'''
# 백준_14712_넴모넴모 (Easy). 골드 5. 풀이: 23.07.07 -> 실패

# How to
## 1. 
전체 경우의 수 - 넴모 없애는 수(네칸에 넴모) = 정답
네칸이 모여있지 않은 경우를 어떻게 판단하지?

## 2. DFS
넴모 네칸이 되는 경우와 아닌 경우를 나누어서 재귀.
x-1, y-1    x-1, y
x, y-1      x, y

## 예제 힌트
2 3
경우의 수: 2^6 = 64
넴모 없애는 수: 6
정답: 64 - 6 = 57

# Review
- 도저히 방법을 모르겠어서 검색하였으나, 잘 이해되지 않았다.
    - 코드 자체가 어렵다기 보다는 "백트래킹"이 아직 낯설다.
- 참고:
https://poroli0119.tistory.com/142
https://health-coding.tistory.com/28

- 계속 문제를 풀다보니, BFS는 그래도 익숙해지는데, DFS와 백트래킹은 너무너무 어렵다.
- 이번 문제는 dfs를 사용하지만, 완전탐색+백트래킹을 이해해야 할것 같다.
- 아무래도 다시 차근차근 풀어봐야겠다..
'''

# 1. 실패 Code
# n, m = map(int, input().split())

# answer = 2**(n*m)

# dx = [0, 1, 1]
# dy = []


# 2. DFS: 실패
n, m = map(int, input().split())
graph = [[True]*m for _ in range(n)]
answer = 0
def dfs(x, y):
    global answer
    
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    
    if (x, y) == (n-1, m-1):
        answer += 1
        return
    
    if 0 <= x-1 < n and 0 <= y-1 < m and (graph[x-1][y-1] or graph[x-1][y] or graph[x][y-1]):
        print(answer, x, y)
        graph[x][y] = False
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        graph[x][y] = True
        
    else:
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        
dfs(0, 0)
print(answer)
    
    
'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''

# # 3. 푸는중
import sys

n, m = map(int, sys.stdin.readline().split())
board = [[False] * m for _ in range(n)]
answer = 0
def dfs(x, y):
    global answer
    
    # 마지막 칸인 경우, 무사히 배치를 성공했으므로 정답 +1
    if (x, y) == (n-1, m-1):
        answer += 1
        return
    
    # 새로운 x, y 좌표 설정
    if y == m-1:
        nx, ny = x+1, 0
    else:
        nx, ny = x, y+1
        
    # 이번 칸을 빈칸으로 놔두고 다음 칸으로 넘어감
    dfs(nx, ny)
    
    # 하나라도 빈칸일 경우, 이번 칸에 넴모를 올리고 다음 칸으로 넘어감
    if not board[x-1][y] or not board[x][y-1] or not board[x-1][y-1]:
        board[x][y] = True
        dfs(nx, ny)
        board[x][y] = False

dfs(1, 1)
print(answer)