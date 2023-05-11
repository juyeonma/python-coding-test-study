# 섬의 개수, 유기농 배추 응용버전이라고 생각!
# 같은 구역이 몇 개인지만 함께 출력해주면 된다고 생각했다.
# 메모리 : 31316KB
# 시간 : 40ms
import sys
input = sys.stdin.readline
n = int(input())

apart = list(list(map(int, input().rstrip())) for _ in range(n))
def dfs(x, y):
    global apart_cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if apart[x][y] == 1:
        apart[x][y] = 0
        # 아파트 구역 숫자 세기
        apart_cnt += 1
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False
data = []
count = 0
for i in range(n):
    for j in range(n):
        # 아파트 구역 개수 초기화
        apart_cnt = 0
        if dfs(i, j):
            count += 1
            data.append(apart_cnt)
print(count)
data.sort()
for i in range(count):
    print(data[i])