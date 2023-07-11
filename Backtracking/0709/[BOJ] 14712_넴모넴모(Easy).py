# 게임의 규칙
# 격자판의 비어 있는 칸을 임의로 골라 “넴모”를 하나 올려놓거나,
# “넴모”가 올라간 칸 네 개가 2 × 2 사각형을 이루는 부분을 찾아 그 위에 있는 “넴모”들을 모두 없애는 것
# 반복
# 격자판 위에 없앨 수 있는 “넴모”가 없으면 게임을 그만두기

# ... 실패...
# 백트래킹 이해했다고 생각했는데 아니었나보다.....
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[0]*(m+1) for _ in range(n+1)]
count = 0


# 백트래킹
def back(depth):
    global count
    if depth == n*m: # 왜 n * m 인지 설명해주실 분...
        count += 1
        return
    
    x = depth // m + 1
    y = depth % m + 1
    back(depth + 1)
    if graph[x - 1][y] == 0 or graph[x][y - 1] == 0 or graph[x - 1][y - 1] == 0:
        graph[x][y] = 1
        back(depth+1)
        graph[x][y] = 0
    
back(0)
print(count)