import sys
from collections import deque
from itertools import permutations
import copy
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
data = [list(map(int, input().split())) for _ in range(k)]
# 342 / 421


def rotation(idx, min_r, min_s, max_r, max_s):
    #
    global arr_copy
    x, y = min_r-1, min_s-1
    k, z = max_r-1, max_s-1
    for i in range(idx):
        dq = deque()
        # 윗면
        for j in range(y+i, z-i):
            dq.append(arr_copy[x+i][j])
        # 오른쪽면
        for j in range(x+i, k-i):
            dq.append(arr_copy[j][z-i])
        # 아랫면
        for j in range(z-i, y+i, -1):
            dq.append(arr_copy[k-i][j])
        # 왼쪽면
        for j in range(k-i, x+i, -1):
            dq.append(arr_copy[j][y+i])

        dq.rotate(1)

        for j in range(y+i, z-i):
            arr_copy[x+i][j] = dq.popleft()
        for j in range(x+i, k-i):
            arr_copy[j][z-i] = dq.popleft()
        for j in range(z-i, y+i, -1):
            arr_copy[k-i][j] = dq.popleft()
        for j in range(k-i, x+i, -1):
            arr_copy[j][y+i] = dq.popleft()


min_value = int(1e9)
for i in permutations(data, k):
    # 342, 421 / 421, 342
    arr_copy = copy.deepcopy(arr)
    for r, c, s in i:
        # 3 4 2
        rotation(min(r+s, c+s) // 2, r-s, c-s, r+s, c+s)
        # 1, 2, 5 , 6
    for j in range(len(arr_copy)):
        if sum(arr_copy[j]) < min_value:
            min_value = sum(arr_copy[j])
print(min_value)

# 시간 빠른 버전.. new_array = 시간 가져오겠습니다..
