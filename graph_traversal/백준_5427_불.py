'''
# 백준_5427_불. 골드 4. 풀이: 23.07.16 -> 실패 -> 성공(2번 풀이)

# How to
- 최단거리, bfs
- 매번 불이 번지고, 상근이가 이동하는걸 각각 반복문으로 처리.
- 이때 매번 불과 상근이의 좌표를 각각 큐로 만들어서, 새로운 큐로 갱신.
- 상근이가 범위를 벗어나는 순간, 즉 건물을 탈출하는 순간 return
- 만약 아무것도 return되지 않았다면, 실패 return

## 2. 성공
- 1의 코드와 유사한데, 불의 확산과 상근이 이동을 별도로 함수로 뺐다.
- 이때, 해당 시간(즉 1초)에서만 불이 확산되고 상근이가 이동할 수 있도록, 매번 시간을 제한하고 갱신했다.

## 반례
1
3 3
*.*
.@.
*.*
정딥: IMPOSSIBLE

# Review
- 풀이 시간:
- 파이썬으로는 시간초과, pypy로 돌려도 메모리 초과.
- 예제도, 반례도 통과했는데 시간초과와 메모리초과.. 어느것에서 줄여야할까??

- 2번 풀이에서 성공하긴 했지만, 전역변수를 너무 남발한듯 하다.
- 차라리 큐에 원소를 3개 넣어서 매번 시간을 재는게 나을까?
'''

# Code
# 1. 실패
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
    
    
# 2. 성공
## 메모리: 76992 KB, 시간: 2184 ms
from collections import deque
import sys
input = sys.stdin.readline

def solve(w, h):
    global fire_cnt, person_cnt
    building = [list(input().rstrip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    fire_q = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire_q.append((i, j))
                fire_cnt += 1
            elif building[i][j] == '@':
                person_q = deque([(i, j)])
                visited[i][j] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 불 확산
    def fire(fire_q):
        global fire_cnt
        cnt = 0
        # 현재 시간에서만 확산
        while fire_cnt:
            x, y = fire_q.popleft()
            fire_cnt -= 1
            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                
                # 땅인 경우, 불이 붙음
                if building[nx][ny] == '.':
                    building[nx][ny] = '*'
                    fire_q.append((nx, ny))
                    cnt += 1
        fire_cnt = cnt

    # 상근이 이동
    def person(person_q):
        global person_cnt
        cnt = 0
        # 현재 시간에서만 확산
        while person_cnt:
            x, y = person_q.popleft()
            person_cnt -= 1
            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j
                # 탈출한 경우, 시간 return
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return visited[x][y] + 1
                
                # 땅이고 방문 전인 경우, 시간 기록
                if building[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y]+1
                    person_q.append((nx, ny))
                    cnt += 1
                    
        person_cnt = cnt
        return 0

    while person_q:
        
        # 불이 존재한다면, 불이 번짐
        if fire_q:  
            fire(fire_q)
            
        # 상근이 이동
        answer = person(person_q)
        # 탈출 했다면, return
        if answer:
            return answer - 1
    
    # 탈출하지 못했다면, 실패
    return "IMPOSSIBLE"

    
for _ in range(int(input())):
    # 너비 w, 높이 h
    w, h = map(int, input().split())
    fire_cnt, person_cnt = 0, 1
    print(solve(w, h))
    