import sys
from collections import deque
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())

d = [u, -d]
visit = [False] * (f+1)
count = 0
def dfs():
    while q:
        x, cnt = q.popleft()
        if x == g:
            return cnt
        for i in range(2):
            nx = d[i] + x
            if nx > f or nx < 1 or visit[nx]:
                continue
            
            visit[nx] = True
            q.append((nx, cnt+1))
    return 'use the stairs'


q = deque()
visit[0] = True
visit[s] = True
q.append((s, 0))
print(dfs())

# 메모리 : 40344 시간 : 480ms