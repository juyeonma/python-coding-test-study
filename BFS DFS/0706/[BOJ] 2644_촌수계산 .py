import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [False] * (n+1)
idx = [-1] * (n+1)
def dfs(x, depth):
    visit[x] = True

    for i in graph[x]:
        if not visit[i]:
            idx[i] = depth + 1
            dfs(i, depth + 1)

dfs(a, 0)
print(idx[b])

# 메모리 : 31256 시간 : 40ms