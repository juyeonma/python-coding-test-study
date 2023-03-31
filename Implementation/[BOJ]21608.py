import sys
input = sys.stdin.readline
n = int(input())

data = [list(map(int, input().split())) for i in range(n**2)]

students = [[0 for _ in range(n)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(n**2):
    student_number = data[i][0]

    map = []
    like_student = data[i][1:]

    for r in range(n):
        for c in range(n):
            if students[r][c] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if students[nr][nc] in like_student:
                            like += 1
                        if students[nr][nc] == 0:
                            blank += 1
                map.append([like, blank, r, c])

    map = sorted(map, key=lambda x: (-x[0], -x[1], x[2], x[3]))
    # like와 blank는 클수록, 행과 열은 작을수록
    students[map[0][2]][map[0][3]] = student_number

cnt = 0
data.sort()
for i in range(n):
    for j in range(n):
        like = 0
        for k in range(4):
            nr, nc = i + dr[k], j+dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if students[nr][nc] in data[students[i][j]-1]:
                    like += 1
        if like != 0:
            cnt += 10 ** (like - 1)
print(cnt)
