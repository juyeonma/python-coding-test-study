# 순열로 간단하게 풀기..!
from itertools import permutations

n, m = map(int, input().split())

for i in permutations(range(1, n+1), m):
    print(*i)
# 메모리 : 31256KB 시간 : 152ms

# 백트래킹으로 풀어보기..! => 다른 사람 풀이 참고..
n, m = map(int, input().split())

arr = [0] * m
visit = [False] * n
def backtracking(n, m, depth):
    if depth == m:
        print(*arr)
        return
    
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            arr[depth] = i+1
            backtracking(n, m, depth+1)

            visit[i] = False
backtracking(n, m, 0)

# 메모리 : 31388KB	시간 : 180ms

# 백트래킹이 더 빠를줄 알았는데.. 내장함수가 더 빨랐다..
# 그래도 백트래킹 조금 이해하기 쉬운 문제였던 것 같다..!