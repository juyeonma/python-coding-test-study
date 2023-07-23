'''
# 백준_1941_소문난 칠공주. 골드 3. 풀이: 23.07.22

# How to
- 조건은 두가지:
    - 총 7명이 가로, 세로로 인접해야함.
    - 4 <= 이다솜파, 임도연파 <= 3

## 1. DFS: 실패

## 2. 조합 후 연결되어 있는지 bfs: 성공
- 7개 좌표들의 조합
    - 0~24의 숫자들의 조합을 구하고, 이를 x, y 좌표로 변환
    - 행: n // 5, 열: n % 5
- 조합마다 매번 방문용 리스트를 새로 만들고, 조합의 좌표들은 모두 False로 설정
    - 좌표의 값이 Y인 경우, 임도연파 +1
    - 만든 방문용 리스트로 bfs를 돌려서, 연결된 좌표들 탐색: 큐의 원소수가 7인지 확인
- 이때, 임도연파(y_cnt)의 인원이 3명 이하이고, 좌표들이 모두 연결되어 있다면 정답 + 1


# Review
- 풀이 시간:
- 처음에 dfs로 실패한 이유는 한 줄로 연결된 것만 탐색하는 바람에 모든 경우의 수를 찾지 못했기 때문이다.
    - 예제처럼 T자 모양으로 갈라진 경우, 재귀에서 되돌아오면서 이미 방문했던 것이 사라지기 때문.
- 그리고, 배열이 5*5로 고정되어 있고 크기가 작으므로, 조합을 구해서 조건을 검사함.
    - 성공하긴 했지만, 너무 느리다.
    
- 다른 사람 풀이를 찾아보니, dfs+bfs 또는 dfs+dfs를 사용하여 매우 빠르게 해결했다.
- 문제 난이도가 높을 수록 dfs나 bfs 단일이 아니라, 이 둘을 복합적으로 또는 중복하여 사용하는 로직이 많아보인다.
    - 아직 골드 3을 풀 때가 아닌가보다.. dfs와 bfs를 혼합하는게 너무 어렵다ㅠ
'''

# Code
# 2. 조합 후 연결되어 있는지 bfs: 성공
## 메모리: 34184 KB, 시간: 2224 ms
from itertools import combinations
from collections import deque
import sys
arr = [list(sys.stdin.readline().rstrip()) for _ in range(5)]

# 7개 좌표들이 모두 연결되어 있는지 검사
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + i, y + j
            
            # 범위를 벗어났거나, 이미 방문했다면
            if nx < 0 or nx > 4 or ny < 0 or ny > 4 or visited[nx][ny]:
                continue
            
            q.append((nx, ny))
            visited[nx][ny] = True
            
    # 연결된 좌표들이 7개가 아닐때, 즉 이번 조합이 모두 인접해 있지는 않을때
    if cnt < 7:
        return False
    
    # 모두 인접해 있다면, 칠공주 결성 성공 
    return True
    
answer = 0
for combi in combinations(range(0, 25), 7):
    visited = [[True]*5 for _ in range(5)]
    y_cnt = 0
    # 이번 조합의 좌표들을 방문할 곳으로 지정
    for i in combi:
        x, y = i // 5, i % 5
        if arr[x][y] == 'Y':
            y_cnt += 1
        visited[x][y] = False
        
    # 인원 수 조건에 어긋나지 않고 연결되어있다면, 칠공주 결성 +1
    if y_cnt <= 3 and bfs(x, y):
        answer += 1

print(answer)
