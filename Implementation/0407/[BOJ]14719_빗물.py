# 풀긴 했는데 속도가 100 나왔다...
# flag를 이용해서 다음 값을 통해서 구분해주었다.
# 다른 사람들의 풀이를 통해 간단한 풀이를 알 수 있어서 좋았다.
import sys
input = sys.stdin.readline
h, w = map(int, input().split())
data = list(map(int, input().split()))

world = [[0] * (h+1) for _ in range(w+1)]
for i in range(w):
    for j in range(h):
        if j < data[i]:
            world[i][j] = 1

count = 0
s = 0
flag = False
for i in range(h):
    for j in range(w):
        if world[j][i] == 1:
            count = 0
            if world[j+1][i] == 0:
                flag = True
        if flag and world[j][i] == 0:
            count += 1
            if world[j+1][i] == 1:
                s += count
                flag = False
    flag = False
    count = 0
print(s)

# hyoyeol6349님의 코드
h, w = map(int, input().split())
heights = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
    left_max = max(heights[:i])
    right_max = max(heights[i+1:])

    compare = min(left_max, right_max)

    if heights[i] < compare:
        ans += compare - heights[i]

print(ans)
