'''
# 백준_17836_공주님을 구해라. 골드 5. 풀이: 23.05.11

# How to
- 조건
    - 1. 벽을 피해서 공주를 구하는 경로
    - 2. 검을 얻고, 벽 파괴하고 공주를 구하는 경로
- 출발지점에서 1칸씩 전진하며 시간을 기록한다. -> BFS
- 중간에 검을 습득했다면, 소요시간과 좌표를 기록한다.
- 그림이 2 이므로, 시간측정은 3부터 시작한다.
- 1. 공주 위치의 값에서 3을 뺀 값이 곧 벽을 피해간 소요 시간.
- 2. 검 위치에서 공주 위치까지 벽을 통과해서 간 시간
- 1과 2 중에서 최솟값이 곧 최종시간. 이때, 제한 시간보다 같거나 작은지 체크한다.

# Review
- 처음에는 bfs 함수 내에서 공주 위치에서의 시간과 검 위치에서의 시간을 전역변수로 구했다.
- 그러나 어짜피 공주는 맨 끝에 있으므로, 그냥 검 위치에서의 시간과 좌표만 기록했다.
- 공주와 검의 위치를 두고 전역변수, 좌표만 등등 다양한 시도를 했지만, 딱히 시간 차이가 크지 않았다.
- 더 시간을 줄일 수 있겠지만.. 지금도 충분히 빠른 시간이라고 생각한다.
'''

# Code
from collections import deque
import sys
input = sys.stdin.readline

# 성: n*m, 제한시간 t
n, m, t = map(int, input().split())

# 0: 빈 공간, 1: 벽, 2: 검
castle = [list(map(int, input().split())) for _ in range(n)]

# 검이 2 이므로, 시간측정은 3부터 시작 -> 나중에 3을 빼서 최종 시간을 계산
castle[0][0] = 3

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 아직 검을 획득하기 전
knife = False

def bfs(x, y):
    global knife
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        cnt = castle[x][y]
        
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            # 성을 벗어나지 않고, 빈칸이거나 검이 있는 경우에
            if 0 <= nx < n and 0 <= ny < m and (castle[nx][ny] == 0 or castle[nx][ny] == 2):
                # 검이 있다면, 검까지의 시간과 좌표 저장
                if castle[nx][ny] == 2:
                    knife = (cnt-2, nx, ny)
                q.append((nx, ny))
                castle[nx][ny] = cnt + 1

bfs(0, 0)

answer = int(1e9)

# 공주 위치에 제한 시간내에 도착했다면
result = castle[n-1][m-1] - 3
if 0 < result <= t:
    answer = result

# 검을 획득했다면
if knife:
    cnt = knife[0] + abs(n-1 - knife[1]) + abs(m-1 - knife[2])
    # 제한 시간내에 공주까지 도착 가능하다면, 정답을 최솟값으로 갱신
    if cnt <= t:
        answer = min(answer, cnt)

# 공주를 구하지 못했다면, 실패
if answer == int(1e9):
    print('Fail')

# 제한시간 내에 공주를 구했다면, 시간 출력
else:
    print(answer)


'''
# Result
풀이 시간: 35분
메모리: 34176 KB
시간: 80 ms
코드 길이: 1078 B
'''