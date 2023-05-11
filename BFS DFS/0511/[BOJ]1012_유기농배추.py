# 1. BFS를 사용해야할까 DFS를 사용해야할까 고민
# 2. 참고 : https://duckracoon.tistory.com/entry/DFS%EC%99%80-BFS-%EA%B0%81%EA%B0%81-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0
# 3. 그래프의 모든 정점을 방문해야하는 문제라고 생각!
# 4. DFS와 BFS를 둘 다 사용 가능?!
# 5. 이코테 -> 음료수 얼려 먹기 문제와 비슷하다고 생각
# 6. DFS로 풀어보았다!

# 메모리 : 31556KB
# 시간 : 56ms
import sys
input = sys.stdin.readline
# 그냥 돌렸을 때 런타임 에러 (RecursionError)가 났다.
# 왜 그런 에러가? 최대 재귀 깊이(1000)보다 재귀의 깊이가 더 깊어졌기 때문!
# 최대 재귀 깊이를 아래 명령어로 바꿔줌
# 1,000,000 정도로 크게 설정해주면 됨
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if matrix[x][y] == 1:
        matrix[x][y] = 0
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = list([0] * m for _ in range(n))
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    count = 0
    for x in range(n):
        for y in range(m):
            if dfs(x, y):
                count += 1
    print(count)

# bfs 풀이 찾아보기
# 찾아본 참고 : https://www.acmicpc.net/source/53151166
# 큰 개념은 dfs와 동일했다..! 
# but 시간은 bfs가 더 빠른 것 같다