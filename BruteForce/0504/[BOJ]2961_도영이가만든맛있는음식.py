# 풀이 방법
# 1. combination으로 모든 조합 찾기
# 2. 곱하기 / 덧셈 각각 하고 답 구하기

# 메모리 : 31256KB
# 시간 : 44MS
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    s, b = map(int, input().split())
    data.append([s, b])

min_value = int(1e9)
for i in range(1, n+1):
    # 1번
    for j in combinations(data, i):
        s_total = 1
        b_total = 0
        # 2번
        for k in range(len(j)):
            s_total *= j[k][0]
            b_total += j[k][1]
        min_value = min(min_value, abs(s_total - b_total))

print(min_value)
