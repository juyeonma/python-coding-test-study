import sys
input = sys.stdin.readline
t = int(input())


def solution1(data, n, r):
    if r < 0:
        r += 8
    while r:
        main = []
        sub = []
        mid_row = []
        mid_col = []
        for i in range(n+1):
            main.append(data[i][i])
            sub.append(data[n-i][i])
            mid_row.append(data[i][n//2])
            mid_col.append(data[n//2][i])
        # 주 대각선 <- 가운데 열
        # 가운데 열 <= 부 대각선
        # 부 대각선 <= 가운데 행
        # 가운데 행 <= 주 대각선
        for i in range(n+1):
            data[i][i], data[i][n//2], data[i][n-i], data[n //
                                                          2][i] = mid_col[i], main[i], mid_row[i], sub[i]
        r -= 1


for _ in range(t):
    n, d = map(int, input().split())
    data = list(input().split() for _ in range(n))
    solution1(data, n-1, d // 45)

    for i in data:
        print(' '.join(i))
