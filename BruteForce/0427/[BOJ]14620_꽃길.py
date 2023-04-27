# 공부가 더 필요하다..ㅜㅜ...
# 아직..백트래킹, dfs에 약한 듯?!
# 참고 : https://dreamtreeits.tistory.com/50
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n = int(stdin.readline())
arr = []
res = [int(1e9)]
visited = set()
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))


def solve(cnt, cost, v):
    if cnt == 3:
        res[0] = min(res[0], cost)

    else:
        # 0 => x, n => x 한칸씩 띄어서 돌리기
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                temp_visit = set()
                temp_visit.add((i, j))
                tf = 1
                temp = arr[i][j]
                # 방향
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if -1 < nx < n and -1 < ny < n:
                        if (nx, ny) not in v:
                            temp += arr[nx][ny]
                            temp_visit.add((nx, ny))
                        else:
                            tf = 0
                            break
                    else:
                        tf = 0
                        break

                if tf and temp_visit:
                    v.update(temp_visit)
                    solve(cnt + 1, cost + temp, v)
                    v -= temp_visit


solve(0, 0, visited)
print(*res)
