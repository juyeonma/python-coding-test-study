'''
# 백준_2194_유닛 이동시키기. 골드 5. 풀이: 23.07.07 -> 실패

# How to
- BFS
- 출발지부터 이동 시작하여 이동 횟수의 최솟값을 갱신한다.
- 매번 상하좌우로 이동 가능한지 탐색한다.
    - 이때 꼭지점 뿐 아니라 한 면이 모두 이동가능해야한다.
    - 이동 가능 하다면, 도착했을 경우 최솟값 갱신하고 도착하지 않았을 경우 큐에 추가하고 방문처리 한다.
- 도착지에 장애물이 존재하거나 도착할 수 없는 경우, -1 출력
- 도착 가능한 경우, 이동 횟수 출력
    
## 반례
도착지에 장애물이 존재하는 경우
정답: -1


# Review
- 계속 4%에서 실패한다. 
    - 예제도 통과하고, 여러 테스트 케이스를 만들어봐도 통과한다. 뭐가 문제일까?
- 꼭지점(좌표 한개)이 아니라, 한 면이 이동 가능한지 여부를 구현하느라 고민했다.
'''

# Code
from collections import deque
import sys
input = sys.stdin.readline

# n*m 맵, a*b 유닛, 장애물 k개
n, m, a, b, k = map(int, input().split())

# 빈 공간: 1로 표시
graph = [[1]*(m+1) for _ in range(n+1)]

# 장애물: 0으로 표시
for _ in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 0

# 출발지, 도착지
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

# 도착지에 장애물이 존재하여 도착할 수 없는 경우, 실패
if not graph[r2][c2]:
    print(-1)
    sys.exit(0)
    
# 상 하 좌 우: 방향(dx, dy), 유닛의 어느 부분인지(xs, ys)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
xs = [[0]*b, [a-1]*b, range(0, a), range(0, a)]
ys = [range(0, b), range(0, b), [0]*a, [b-1]*a]
'''
r1, c1:c1+b
r1+a-1, c1:c1+b
r1:r1+a, c1
r1:r1+a, c1+b-1
'''

answer = 250000

def bfs(x, y):
    global answer
    q = deque([(x, y, 0)])
    graph[x][y] = 0
    while q:
        x, y, cnt = q.popleft()
        for i, j, ix, jy in zip(dx, dy, xs, ys):
            # 유닛의 다음 꼭지점 기록
            next_x, next_y = x + ix[0] + i, y + jy[0] + j
            # 꼭지점 뿐 아니라 해당 면이 모두 이동 가능해야한다.
            for iix, jjy in zip(ix, jy):
                nx = x + iix + i
                ny = y + jjy + j
                
                # 범위를 벗어났다면, break
                if nx < 1 or nx > n or ny < 1 or ny > m:
                    break
                
                # 장애물이면, break
                if not graph[nx][ny]:
                    break
    
            # 이동 가능 하다면,
            else:
                # 도착했을 경우, 최솟값 갱신
                if (next_x, next_y) == (r2, c2):
                    answer = min(answer, cnt+1)
                    continue
                
                # 도착하지 않았을 경우, 큐에 추가하고 방문 처리(=장애물로 기록)
                q.append((next_x, next_y, cnt+1))
                graph[nx][ny] = 0
                
# 출발지부터 이동 시작
bfs(r1, c1)

# 도착할 수 없다면, 실패
if answer == 250000:
    print(-1)

# 도착할 수 있다면, 이동 횟수 출력
else:
    print(answer)


'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''