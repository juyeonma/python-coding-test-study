# DFS인가 BFS인가부터 감이 안왔다..ㅠㅠ..
# 결국 답 참고..https://ryu-e.tistory.com/39
# 시간 : 212ms
# 메모리 : 58352KB
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
water = list(map(int, input().split()))
visited = set()
q = deque()

# 1. 샘터를 기준으로 시작하기 위해 큐에 넣어줌
for i in water:
    q.append((i, 1))
    visited.add(i)

# 2. -1, +1 위치 방향으로 bfs 진행
result = 0
now_build = 0
def bfs(q):
    global result, now_build
    while q:
        now, b = q.popleft()
        for d in [1, -1]:
            nx = now + d
            if nx in visited:
                continue

            visited.add(nx)
            result += b
            now_build += 1
            q.append((nx, b+1))
            if now_build == k:
                q = list()
                break
bfs(q)
print(result)