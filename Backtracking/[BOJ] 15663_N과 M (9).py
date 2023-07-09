# 순열로 풀기
from itertools import permutations

n, m = map(int, input().split())
data = list(map(int, input().split()))

result = []
for i in permutations(data, m):
    result.append(i)


result = list(set(result))
result.sort()
for i in result:
    print(*i)

# 메모리 : 38260	시간 : 108ms

# 백트래킹으로 풀기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
arr = [0] * m
visit = [False] * n

result = []
def backtracking(n, m, depth):
    if depth == m:
        result.append(arr[:])
        return
    
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            arr[depth] = data[i]
            backtracking(n, m, depth+1)

            visit[i] = False

backtracking(n, m, 0)

result = list(set(map(tuple, result)))
result.sort()
for i in result:
    print(*i)

# 메모리 : 41332KB 시간 : 152ms