'''
# 백준_1743_음식물-피하기. 실버 1. 풀이: 23.09.15

# How to
- 쓰레기의 위치를 통로(board)와 쓰레기 모음(trash)에 추가
- BFS로 각각의 쓰레기마다 덩어리 크기를 재고, 정답을 갱신
    - 연결된 쓰레기를 큐에 넣을 때마다 쓰레기를 치워야(즉 0으로 바꿔줘야) 중복 방지됨

# Review
- 풀이 시간: 20분
'''

# Code
# 1. BFS
## 메모리: 34176 KB, 시간: 80 ms 
from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
# board: 통로 배열, trash: 쓰레기 위치만 모아놓음
board = [[0]*m for _ in range(n)]
trash = []

for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
    trash.append((r-1, c-1))
    
def bfs(i, j):
    q = deque([(i, j)])
    board[i][j] = 0
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i, j in zip([1,-1,0,0], [0,0,1,-1]):
            nx, ny = x+i, y+j
            # 범위 안이고, 쓰레기일 경우, 큐에 추가 후 쓰레기 치움(중복 방지)
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
                q.append((nx, ny))
                board[nx][ny] = 0
                
    return cnt

# 각각의 쓰레기마다 덩어리 크기를 측정하고 정답 갱신
answer = 0
for i, j in trash:
    answer = max(answer, bfs(i, j))

print(answer)