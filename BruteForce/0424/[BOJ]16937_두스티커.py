# 전체 경우를 리스트에 넣은 것 까지는 구현..!
# 그 후 더하기 부분을 생각하지 못했다..
import sys
from itertools import permutations
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
data = []
for _ in range(n):
    r, c = map(int, input().split())
    data.append((r, c))
sticker = (list(permutations(data, 2)))
result = 0
for i, j in sticker:
    r1, c1 = i[0], i[1]
    r2, c2 = j[0], j[1]
    if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
        result = max(result, r1*c1 + r2*c2)
    if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
        result = max(result, r1*c1 + r2*c2)
    if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
        result = max(result, r1*c1 + r2*c2)
    if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
        result = max(result, r1*c1 + r2*c2)
print(result)
