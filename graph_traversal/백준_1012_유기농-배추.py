'''
# 백준_1012_유기농 배추. 실버 2. 풀이: 23.05.09

# 풀이방법
- 이코테 음료수 얼려먹기 문제랑 똑같다!
- 먼저 DFS로 풀고, BFS로도 풀어봤다.

## DFS 풀이
- 배추 좌표만 따로 저장하여 탐색한다.
- DFS가 True일 경우, 즉 처음 방문하는 배추라면 정답을 +1 한다.
- DFS 함수
    - 처음 방문하는 배추일 경우: 방문 처리 ->  상하좌우로 dfs를 재귀적으로 호출 -> True return
    - 배추가 없거나 이미 방문한 배추일 경우: False return
    - 상하좌우의 위치를 재귀적으로 호출하면서 배추일 경우 방문 처리를 하기 때문에, 한번 dfs를 거치면 이어진 배추들은 전부 방문처리가 된다.

## BFS 풀이
- 배추 좌표만 따로 저장하여 탐색한다.
- 방문 전인 배추라면, BFS에 넣어서 방문 처리 후 정답을 +1 한다.
- BFS 함수
    - 현재 배추 위치를 큐에 넣고, 방문 처리 한다.
    - 상하좌우를 살피며 아직 방문 전인 배추가 있다면, 방문처리하고 큐에 넣는다.

# 보완할 것
- DFS에서 최대 재귀 깊이를 조심하자!
    - RecursionError가 발생하여, sys.setrecursionlimit(10**6)로 최대 재귀 깊이 제한을 늘렸다.
'''

# DFS 풀이
import sys
# 최대 재귀 깊이 제한을 늘림
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# DFS 함수: x, y 좌표를 방문 처리하고, 상하좌우를 방문
def dfs(x, y, dic):
    if (x, y) in dic and dic[(x, y)]:
        dic[(x, y)] = False # 방문 처리
        dfs(x+1, y, dic)
        dfs(x-1, y, dic)
        dfs(x, y+1, dic)
        dfs(x, y-1, dic)
        return True
    return False

def solve():
    # k: 배추 갯수
    *_, k = map(int, input().split())
    
    # key는 배추 위치로, value는 True로 해서 dictionary를 만든다.
    dic = dict(zip([tuple(map(int, input().split())) for _ in range(k)], [True]*k))
    answer = 0
    for x, y in dic:
        # True라면, 즉 배추를 처음 방문한다면, 정답 +1
        if dfs(x, y, dic):
            answer += 1
    return answer

# 테스트 케이스 갯수만큼 출력
for i in range(int(input())):
    print(solve())


# BFS 풀이
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
    
# BFS 함수: queue에 현재 배추 좌표를 넣고, 방문처리.
def bfs(x, y, dic):
    q = deque([[x, y]])
    dic[(x, y)] = False
    
    while q:
        x, y = q.popleft()
        # 상하좌우에 아직 방문 전인 배추가 있다면, 방문처리하고 큐에 넣음
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in dic and dic[(nx, ny)]:
                dic[(nx, ny)] = False
                q.append([nx, ny])

def solve():
    # k: 배추 갯수
    *_, k = map(int, input().split())
    
    # key는 배추 위치로, value는 True로 해서 dictionary를 만든다.
    dic = dict(zip([tuple(map(int, input().split())) for _ in range(k)], [True]*k))

    answer = 0
    for (x, y), value in dic.items():
        # True라면(아직 방문 전이면), 배추를 방문처리하고, 정답 +1
        if value:
            bfs(x, y, dic)
            answer += 1
    return answer

# 테스트 케이스 갯수만큼 출력
for i in range(int(input())):
    print(solve())
        

'''
# 결과
## DFS
메모리: 31572 KB
시간: 60 ms
코드 길이: 617 B

## BFS
메모리: 34176 KB
시간: 72 ms
코드 길이: 790 B
'''