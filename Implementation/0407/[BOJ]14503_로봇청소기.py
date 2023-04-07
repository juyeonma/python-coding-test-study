# 문제 분석
# 시간 제한 : 2초
# 최대 : 50 최소 : 3
# 메모리 512.
# 문제 구현
# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
# 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
# 3-1. 반시계 방향으로 90도 회전한다.
# 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 3-3. 1번으로 돌아간다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [[0] * m for _ in range(n)]
data = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 0 : 북  1 : 동 2 : 남 3 : 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


arr[r][c] = 1
count = 1
turn_time = 0
while True:
    turn_left()
    nx = r + dx[d]
    ny = c + dy[d]
    if data[nx][ny] == 0 and arr[nx][ny] == 0:
        r = nx
        c = ny
        arr[r][c] = 1
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if data[nx][ny] == 0:
            r = nx
            c = ny
        else:
            break
        turn_time = 0
print(count)
