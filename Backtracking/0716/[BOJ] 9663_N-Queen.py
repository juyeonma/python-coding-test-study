# 시간 초과 코드..
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

chess = [[False]*n for _ in range(n)]

data= []
ex = []
count = 0
def back(x, y):
    global count
    if len(data) == n:
        count += 1
        return

    for i in range(x+1, n):
        for j in range(n):
            if j == y or j in ex:
                continue
            flag = False
            for nx, ny in data:
                for k in range(n-nx):
                    if i == nx+k and j == ny+k:
                        flag = True
                        break
                    if i == nx+k and j == ny - k:
                        flag = True
                        break
                if flag:
                    break
            if not flag:
                data.append((i, j))
                ex.append(j)
                back(i, j)
                ex.pop(-1)
                data.pop(-1)

back(0, 0)
for i in range(n):
    data.append((0, i))
    ex.append(i)
    back(0, i)
    ex.pop(-1)
    data.pop()
print(count)





# 참고 보기 : https://www.acmicpc.net/source/28613974
# 이해..할려고 노력중입니다...ㅜ
import sys

def nQueen(row, di1, di2, i, N):
    answer = 0

    for c in range(N):
        if row[c] != 1 and di1[i - c + N] != 1 and di2[i + c] != 1:
            if i + 1 == N: answer += 1
            else :
                row[c] = 1; di1[i - c + N] = 1; di2[i + c] = 1
                answer += nQueen(row, di1, di2, i + 1, N)
                row[c] = 0; di1[i - c + N] = 0; di2[i + c] = 0

    return answer

def solution(N):
    row = [0 for _ in range(N)]
    di1 = [0 for _ in range(2 * N)]
    di2 = [0 for _ in range(2 * N)]

    answer = 0
    for c in range(N // 2):
        if row[c] != 1 and di1[N - c] != 1 and di2[c] != 1:
            if N == 1: answer += 1
            else :
                row[c] = 1; di1[N - c] = 1; di2[c] = 1
                answer += nQueen(row, di1, di2, 1, N)
                row[c] = 0; di1[N - c] = 0; di2[c] = 0
    answer *= 2

    if N % 2 == 1:
        c = N // 2
        if row[c] != 1 and di1[N - c] != 1 and di2[c] != 1:
            if N == 1: answer += 1
            else :
                row[c] = 1; di1[N - c] = 1; di2[c] = 1
                answer += nQueen(row, di1, di2, 1, N)
                row[c] = 0; di1[N - c] = 0; di2[c] = 0

    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    # import time
    # start = time.time()
    sys.stdout.write('%d\n'%solution(N))
    # print("time :", time.time() - start)