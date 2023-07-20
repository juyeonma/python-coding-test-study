'''
# 백준_5427_불. 골드 4. 풀이: 23.07.16 -> 실패

# How to
- 최단거리, bfs
- 매번 불이 번지고, 상근이가 이동하는걸 각각 반복문으로 처리.
- 이때 매번 불과 상근이의 좌표를 각각 큐로 만들어서, 새로운 큐로 갱신.
- 상근이가 범위를 벗어나는 순간, 즉 건물을 탈출하는 순간 return
- 만약 아무것도 return되지 않았다면, 실패 return

## 반례

# Review
- 풀이 시간:
- 파이썬으로는 시간초과, pypy로 돌려도 메모리 초과.
- 예제도, 반례도 통과했는데 시간초과와 메모리초과.. 어느것에서 줄여야할까??
'''

# Code
# 1.
## 메모리:  KB, 시간:  ms
from collections import deque
import sys
input = sys.stdin.readline

def solve(w, h):
    building = [list(input().rstrip()) for _ in range(h)]
    fire_q = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                sx, sy = i, j
                building[i][j] = '#'
            elif building[i][j] == '*':
                fire_q.append((i, j))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    person_q = deque([(0, sx, sy)])
    
    def bfs(person_q, fire_q):
        while person_q:
            
            # 불이 번짐
            n_fire_q = fire_q.copy()
            while fire_q:
                fire_x, fire_y = fire_q.popleft()
                for i, j in zip(dx, dy):
                    nx, ny = fire_x + i, fire_y + j
                    if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.':
                        building[nx][ny] = '*'
                        n_fire_q.append((nx, ny))

            fire_q = n_fire_q
                
            # 상근이 이동
            n_person_q = deque()
            while person_q:
                t, x, y = person_q.popleft()
                building[x][y] = '#'
                
                for i, j in zip(dx, dy):
                    nx, ny = x + i, y + j
                    if nx < 0 or nx >= h or ny < 0 or ny >= w:
                        return t+1
                    
                    if building[nx][ny] == '.':
                        n_person_q.append((t+1, nx, ny))
                
            person_q = n_person_q
            
        return "IMPOSSIBLE"
    
    return bfs(person_q, fire_q)
    
for _ in range(int(input())):
    # 너비 w, 높이 h
    w, h = map(int, input().split())
    print(solve(w, h))