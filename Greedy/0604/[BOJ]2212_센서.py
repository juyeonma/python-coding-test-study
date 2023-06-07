# import sys
# from itertools import combinations
# input = sys.stdin.readline
# n = int(input())
# k = int(input())
# data = [*map(int, input().split())]
# data = list(set(data))
# data.sort()

# min_value = 1e9
# for com in combinations(data, k):
#     total = [1e9] * len(data)
#     for i in com:
#         for j in range(len(data)):
#             if total[j] > abs(data[j] - i):
#                 total[j] = abs(data[j] - i)
#     min_value = min(sum(total), min_value)

# print(min_value)

# 시간 초과.. => 규칙을 찾았어야 했는데.. 찾지못함..
# 참고 : https://journeytosth.tistory.com/16
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
data = [*map(int, input().split())]
data.sort()
if k>=n:
    print(0)
    sys.exit()

dist = []
for i in range(1, n):
    dist.append(data[i] - data[i-1])

dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))

# 설명을 보니 매우 쉬운 문제였다..