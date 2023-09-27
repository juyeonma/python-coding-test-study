'''
# 백준_13549_숨바꼭질3. 골드 5. 풀이: 23.09.15

# How to
- BFS
- 걷거나 or 순간이동 하면서
    - 소요 시간 갱신, 큐에 추가(타겟으로 계속 이동)

## 예제
5 17
10 9 18 17 => 2초
10 20 19 18 17 => 3초

# Review
- 풀이 시간: 숨바꼭질2 풀고 바로. 10분?
- 실수로 숨바꼭질2를 먼저 풀고나서 숨바꼭질3를 풀었는데, 거의 유사해서 바로 풀었다.
- 다만 시간이 빠르진 않는데, 맞힌 사람을 보니까 k < n인 경우는 순간이동을 못한다는 조건을 추가해야했다.
'''

# Code
# 1. BFS: 성공
## 메모리: 46160 KB, 시간: 140 ms
from collections import deque
n, k = map(int, input().split())

# 수빈이의 위치별 소요시간과 경우의 수 딕셔너리
subin = {n: 0}

def bfs(x, target):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == target:
            return subin[x]
        
        # 걷거나 순간이동 하면서
        for nx, a in [(x+1, 1), (x-1, 1), (2*x, 0)]:
            if 0 <= nx <= 100_000:
                # nx가 처음이거나 더 낮은 소요 시간이면,
                # 소요 시간 갱신, 큐에 추가
                if nx not in subin or subin[x]+a < subin[nx]:
                    subin[nx] = subin[x] + a
                    q.append(nx)
                    
print(bfs(n, k))
