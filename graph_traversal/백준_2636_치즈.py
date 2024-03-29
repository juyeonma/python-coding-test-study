'''
# 백준_2636_치즈. 골드 4. 풀이: 23.05.12 -> 구글링 후 성공

# How to
- 출력: 치즈가 모두 녹는 시간, 녹기 1시간 전 치즈 칸 수
- BFS: 공기에서 출발하여, 사방을 살펴본다.
    - 치즈라면, 녹을 치즈로 분류.
    - 공기라면, 큐에 추가.
    - 치즈가 1로 표시되므로, 방문표시는 2로 한다.
- 큐가 비게 되면, 녹을 치즈를 공기로 바꾸고, 이 녹을 치즈 큐를 반환한다.
- 매번 bfs에서 두개가 반환된다
    - 녹을 치즈 길이: 곧 매 시간 녹는 치즈 갯수
    - 녹을 치즈 큐: 다음번 bfs에서 출발할 큐
- 모든 치즈가 녹을때까지 bfs를 반복한다.
    - 이때, 출발 좌표(즉, 큐의 첫번째 원소)를 0, 0 으로 해도 되지만, 똑같은 공기를 탐색하게 된다.
    - 따라서 이전 시간의 녹을 치즈, 즉 이번 시간에서 공기가 된 부분을 시작 큐로 하면 시간을 절약할 수 있다.

# Review
- 모르겠으면 바로 답을 찾아보자고 결심했지만, 이 문제는 오기가 생겨서 몇시간이고 붙잡았다.. 결국 아이디어를 구글링 했지만 ㅠㅠ
- 구멍을 어떻게 판별할 것인가?를 고민했고, 이를 따로 함수로 구현하려고 했다...
- 결국 구글링 해서, 아이디어를 얻어서 풀었다.
    - bfs에 파라미터로 들어가는 큐 이외에 별도의 큐에 녹는 치즈를 담고, 이 큐가 그 다음번 bfs의 파라미터로 들어간다. 
    - "큐는 한개만"이라는 고정관념이 있었는지, 이 문제에서 큐를 하나 더 만들어서 갱신한다는 아이디어가 너무 신선한 충격이었다.
- sys.stdin.readline 를 했더니 미미하지만 메모리와 시간이 증가했다. 왜지..?
- pypy로 돌렸더니 메모리 116680 KB, 시간 188 ms이 나왔다. pypy가 무조건 빠른게 아니구나..?
'''

# Code
from collections import deque

# 행, 열
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(q):
    # 녹을 치즈를 담을 빈 큐 생성
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            # 범위 안에 있고, 방문하지 않았다먼
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] < 2:
                # 치즈라면, 녹을 치즈에 추가
                if graph[nx][ny]:
                    melt.append((nx, ny))
                # 공기라면, 큐에 추가
                else:
                    q.append((nx, ny))
                # 방문 표시
                graph[nx][ny] = 2
    # 치즈 녹이기: 치즈를 공기로 변환
    for x, y in melt:
        graph[x][y] = 0

    # 이번 시간에서의 녹은 치즈 갯수와 녹은 치즈 좌표가 담긴 큐를 반환
    return len(melt), melt

x, y = 0, 0
# 전체 치즈 갯수
all_cheese = sum(map(sum, graph))
time = 0
q = deque([(0, 0)])
while all_cheese:
    cnt, q = bfs(q)
    # 남은 치즈 갯수 갱신: 전체 치즈 갯수 - 이번 시간에서 녹은 치즈
    all_cheese -= cnt
    # 시간 1 증가
    time += 1
    
# 소요 시간과 다 녹기 1시간 전의 치즈 갯수 출력
print(time)
print(cnt)

'''
# Result
풀이 시간: 2시간 +@
메모리: 34160 KB
시간: 64 ms
코드 길이: 816 B
'''