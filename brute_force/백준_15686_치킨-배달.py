'''
# 백준_15686_치킨 배달. 골드 5. 풀이: 23.05.05

# 풀이방법
- 예전에 이코테 풀었던 문제라서 금방 풀었다.
- 모든 치킨 조합에 대해서 모든 집에서의 치킨 거리를 구하고, 최솟값으로 갱신하고, 각 집의 거리를 더하는 것.
'''

'''
# 보완할 것
- 시간이 너무 오래 걸린다.
- 생각해보니.. 치킨거리가 계속 중복해서 계산된다. 이걸 줄이면 시간도 확 줄거같다.
- 어떻게 해야할까?
'''

# 풀이 기록
# 행렬 n*n, 치킨집 최대 m개
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

house, chicken = [], []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1: # 집
            house.append((i, j))
        elif tmp[j] == 2: # 치킨집
            chicken.append((i, j))

arr = list(combinations(chicken, m))

answer = int(1e9)
for chicks in arr:
    result = 0
    for x, y in house:
        tmp = int(1e9)
        for a, b in chicks:
            tmp = min(tmp, abs(x-a) + abs(y-b))
        result += tmp
    answer = min(answer, result)

print(answer)

'''
# 결과
메모리: 31256 KB
시간: 612 ms
코드 길이: 634 B
'''