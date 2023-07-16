'''
# 백준_5014_스타트링크. 실버 1. 풀이: 23.07.12

# How to
- 최단거리를 구하는 것이므로, BFS
- 현재층에서 이동거리 0에서 출발
- 매번 목적지에 도착했는지 체크하고, 맞다면 이동 횟수를 return 하여 출력
- 매번 위로 올라가거나 or 내려갈 수 있는지(즉 범위 안이고 방문 전인지) 체크하여, 큐에 추가하고 방문 처리.


## 반례
20 20 1 1 4
답: 6

1000000 1000000 1 0 1
답: 999999

# Review
- 풀이 시간: DFS 1시간, BFS 20분
- DFS에 약해서, 최단거리지만 DFS로 도전했다가 역시나 시간초과로 실패했다.
- BFS로 푸니, 전형적인 BFS였다.
'''

# Code
# 2. BFS: 성공
## 메모리: 40248 KB, 시간: 440 ms

from collections import deque

# 건물: f층, 현재: s층, 스타트링크: g층, 위로 u, 아래로 d
f, s, g, u, d = map(int, input().split())
visited = [False] * (f+1)
visited[s] = True

def bfs(q):
    while q:
        cnt, s = q.popleft()
        # 목적지에 도착했다면, 이동횟수 return
        if s == g:
            return cnt
        
        # 올라가거나 or 내려가거나
        for i in [u, -d]:
            ns = s + i
            # 범위 안이고 방문 전이라면, 큐에 추가하고 방문 처리
            if 0 < ns <= f and not visited[ns]:
                q.append((cnt+1, ns))
                visited[ns] = True
    
    # 큐가 빌 때까지 도착하지 못했다면, 실패
    return "use the stairs"

print(bfs(deque([(0, s)])))


# 1. DFS: 실패. 시간초과
import sys
sys.setrecursionlimit(10000000)

# 건물: f층, 현재: s층, 스타트링크: g층, 위로 u, 아래로 d
f, s, g, u, d = map(int, input().split())
visited = [False] * (f+1)
visited[0] = True

answer = int(1e9)

def dfs(now, cnt):
    global answer
    
    # 스타트링크에 도착한 경우, 이동횟수 갱신
    if now == g:
        answer = min(answer, cnt)
        return

    if 0 <= now+u <= f and not visited[now+u]:
        visited[now+u] = True
        dfs(now+u, cnt+1)
        visited[now+u] = False
        
    if 0 <= now-d <= f and not visited[now-d]:
        visited[now-d] = True
        dfs(now-d, cnt+1)
        visited[now-d] = False

# 현재 s층, 이동 0번
visited[s] = True
dfs(s, 0)

if answer != int(1e9):
    print(answer)
else:
    print("use the stairs")
