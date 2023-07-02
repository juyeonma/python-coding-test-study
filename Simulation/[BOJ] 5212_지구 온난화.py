r, c = map(int, input().split())

map = [list(input()) for _ in range(r)]

clone_map = [['.'] * c for _ in range(r)]
def check(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < r and 0 <= ny < c:
            if map[nx][ny] == '.':
                cnt += 1
        else:
            cnt += 1

    if cnt < 3:
        clone_map[x][y] = 'X'

for i in range(r):
    for j in range(c):
        if map[i][j] == 'X':
            check(i, j)

min_x, min_y = r, c
max_x, max_y = 0, 0
for i in range(r):
    for j in range(c):
        if clone_map[i][j] == 'X':
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)

for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        print(clone_map[i][j], end = '')
    print()


# 메모리 : 	31256	시간 : 44