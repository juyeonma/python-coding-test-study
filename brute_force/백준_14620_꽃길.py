'''
# 백준_14620_꽃길. 실버 2. 풀이: 23.04.24

# 풀이방법
- 제한 2가지
    - 테두리에는 심으면 안된다. (화단 밖으로 꽃잎이 나가는걸 방지)
    - 두 씨앗의 최소 거리는 3(꽃잎이 닿는것 방지)

- 1) 방법
    - 모든 씨앗 조합에 대해 비용을 구해서 갱신.
1. 씨앗 3개 심을 자리 조합
2. 조합을 탐색
3. 꽃이 겹치면(거리 < 3) 넘어감
4. 배열을 벗어나지 않으면, 비용을 구하고 갱신.
'''

'''
# 보완할 점
- 시간 복잡도를 줄이자.
- 1) 방법과 같은데, 순서를 달리하면 어떨까? 씨앗당 비용을 먼저 구하고, 조합을 탐색하여 최솟값 갱신.
'''

# code
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 1. 씨앗 3개 심을 자리 조합
combs = list(combinations(range(n*n), 3))        

# 씨앗을 심었을 때, 5곳(동서남북+씨앗)의 비용 합
def sum_cost(x, y):
    result = arr[x][y]
    for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        result += arr[x+i][y+j]
    return result 

answer = 1e9
# 2. 조합을 탐색
for a, b, c in combs:
    # i*n + j
    x1, y1 = a // n, a % n
    x2, y2 = b // n, b % n
    x3, y3 = c // n, c % n

    # 3. 꽃이 겹치면(거리 < 3) 넘어감
    if abs(x1-x2) + abs(y1-y2) < 3 or abs(x1-x3) + abs(y1-y3) < 3 \
        or abs(x2-x3) + abs(y2-y3) < 3:
        continue
  
    # 4. 배열을 벗어나지 않으면, 비용을 구하고 갱신.
    if 0 < x1 < n-1 and 0 < x2 < n-1 and 0 < x3 < n-1 \
        and 0 < y1 < n-1 and 0 < y2 < n-1 and 0 < y3 < n-1:
        # 씨앗 3개 비용을 구함
        cost = sum_cost(x1, y1) + sum_cost(x2, y2) + sum_cost(x3, y3)
        answer = min(answer, cost)

print(answer)

'''
# 결과
메모리: 42904 KB
시간: 324 ms
코드 길이: 848 B
'''