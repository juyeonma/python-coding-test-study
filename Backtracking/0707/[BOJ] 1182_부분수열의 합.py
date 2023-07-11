from itertools import combinations
import sys
input = sys.stdin.readline
n, s = map(int, input().split())

data = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    for j in combinations(data, i):
        if sum(j) == s:
            count += 1

print(count)

# 	메모리 : 31256	시간 : 352ms

# 백트래킹
def backtracking(m, depth, begin):
    global count
    if m == depth:
        if s == sum(arr):
            count += 1
        return
    for i in range(begin, n):
        arr[depth] = data[i]
        backtracking(m, depth+1, i+1)
for i in range(1, n+1):
    arr = [0] * i
    backtracking(i, 0, 0)
print(count)

# 메모리 : 31256	시간 : 2784ms