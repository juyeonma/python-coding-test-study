'''
# 백준_2583_영역 구하기. 실버 1. 풀이: 23.07.06

# How to
- BFS
- 주어진 직사각형은 전부 방문 처리
- 빈 공간이 있으면, bfs로 탐색하여 연결된 빈 공간의 개수를 정답 리스트에 추가
    - 연결된 빈 공간을 전부 탐색
    - 매번 사방을 탐색해서, 범위 안 & 빈 공간이라면: 큐에 추가, 방문 처리, 개수 +1
    - 탐색이 끝나면, 연결된 빈 공간의 개수 return
 
# Review
'''

# Code
from collections import deque
import sys
input = sys.stdin.readline
    
def bfs(paper, x, y):
    # x, y 부터 탐색 시작. 방문처리하고, 개수 = 1
    q = deque([(x, y)])
    paper[x][y] = False
    cnt = 1
    
    # 연결된 빈 공간을 전부 탐색
    while q:
        x, y = q.popleft()
        
        for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx = x + i
            ny = y + j

            # 범위 안 & 빈 공간이라면, 큐에 추가, 방문 처리, 개수 +1
            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny]:
                q.append((nx, ny))
                paper[nx][ny] = False
                cnt += 1

    # 연결된 빈 공간의 개수 return
    return cnt

# 행: n, 열: m
m, n, k = map(int, input().split())
paper = [[True] * m for _ in range(n)]

# 직사각형 표시
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            paper[x][y] = False
    
answer = []
for x in range(n):
    for y in range(m):
        # 방문하지 않은 빈 공간이라면, bfs로 연결된 빈 공간의 개수 세기
        if paper[x][y]:
            answer.append(bfs(paper, x, y))
            
print(len(answer))
print(*sorted(answer))


'''
# Result 
풀이 시간: 20분
메모리: 34184 KB
시간: 68 ms
코드 길이: 1182 B
'''