n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# ...답..참고... : https://comdolidol-i.tistory.com/313
shape = {0 : [0, -1, 1, 0], 1 : [-1, 0, 0, -1], 2 :[-1, 0, 0, 1], 3 : [0, 1, 1, 0]}
visited = [[False] * m for _ in range(n)]
answer = 0
def dfs(i, j, sum):
    global answer
    if j == m: 
        i += 1
        j = 0
    if i == n:
        answer = max(answer, sum)
        return
    
    if not visited[i][j]:
        for k in range(4):
            a, b, c, d = shape[k]
            x, y, xx, yy = i + a, j + b, i + c, j + d
            if 0 <= x < n and 0 <= xx < n and 0 <= y < m and 0 <= yy < m and not visited[x][y] and not visited[xx][yy]:
                visited[x][y] = visited[xx][yy] = visited[i][j] = True
                dfs(i, j+1, sum + data[i][j] * 2 + data[x][y] + data[xx][yy])
                visited[i][j] = visited[x][y] = visited[xx][yy] = False
    dfs(i, j + 1, sum)
dfs(0, 0, 0)
print(answer)

# 다시 풀기..