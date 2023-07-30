# # 시간초과 코드.... 83%에서 시간초과였다(pypy는 통과는 했어요..)
import sys
input = sys.stdin.readline
sudoku = list(list(map(int, input().split())) for _ in range(9))
temp = []

# 0 좌표 찾고 find에 저장
find = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            find.append([i, j])

# 스도쿠 세로
for i in range(9):
    d = []
    for j in range(9):
        d.append(sudoku[j][i])
    temp.append(d)

def check(x, y):
    center_x = (x // 3) * 3 + 1
    center_y = (y//3) * 3 + 1
    for i in range(center_x-1, center_x+2):
        for j in range(center_y-1, center_y+2):
            if i == x and j == y:
                continue
            if sudoku[x][y] == sudoku[i][j]:
                return False
    return True
# 숫자들 찾기
def back(k):
    if k == len(find):
        for n in range(9):
            print(*sudoku[n])
        sys.exit(0)
    
    x, y = find[k][0], find[k][1]

    answer = []

    for num in range(1, 10):
        if num not in sudoku[x] and num not in temp[y]:
            answer.append(num)
    
    if len(answer) == 0:
        return
    
    for ans in answer:
        sudoku[x][y] = ans
        temp[y][x] = ans
        if check(x, y):
            back(k+1)
    sudoku[x][y] = 0
    temp[y][x] = 0
back(0)


# 참고 => 주연님이랑 재훈님 코드 보고 이해중입니다....