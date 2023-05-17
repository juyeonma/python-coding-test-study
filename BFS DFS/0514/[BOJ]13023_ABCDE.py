# 친구 관계가 => DFS 깊이 탐색이라고 생각!
# 백트래킹까지는 생각을 했는데.. 구현 실패..!
# 깊이 => depth가 중요했는데 그 부분을 생각하지 못해서이다..ㅠ
# 참고 : https://data-flower.tistory.com/104

# 메모리 : 31256KB
# 시간 : 1796ms
# 시간은 왜 오래 걸렸을까..
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
ans = False
def dfs(start, depth):
    global ans
    visited[start] = True

    if depth == 4:
        ans = True
        return
    
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth+1)
            visited[i] = False

visited = [False]*n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break

if ans:
    print(1)
else:
    print(0)