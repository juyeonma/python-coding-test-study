# 유기농 배추 문제랑 비슷하다고 생각했다..!
# 인접한 구역은 => 같은 구역
# 유기농 배추처럼 dfs 사용

# 메모리 : 31540KB
# 시간 : 76ms
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    
    if data[x][y] == 1:
        data[x][y] = 0
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        # 대각선 부분 포함
        dfs(x-1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y-1)
        dfs(x+1, y+1)
        return True
    
    return False
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    data = list(list(map(int, input().rstrip().split())) for _ in range(h))
    
    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                count += 1
    print(count)