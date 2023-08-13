'''
# 백준_12738_가장 긴 증가하는 부분 수열 3. 골드 2. 풀이: 23.08.13

## LIS: 최장 증가 부분 수열을 이용한 문제들
- DP로 풀면, 시간복잡도가 크다: O(n^2)
- 따라서 시간복잡도를 개선하기 위해 이분 탐색을 활용해야한다: O(nlogn)
- 백준에서는 입력의 최댓값에 따라 유형이 나뉜다.
    - dp: 11053, 14002, 11054, 11055, 11722
    - 이분탐색: 12015, 12738, 14003
-> dp와 이분탐색의 두 방법으로 풀어보자

# How to
- 역시나 입력값이 매우 크고(1,000,000) 음수가 주어지며, LIS의 길이를 묻는 질문.
    - 따라서 bisect 사용

# Review
- 풀이 시간: 5분
'''

# Code
# DP -> 시간초과 확정이라, 코드 구현 안함

# 1. 이분탐색 bisect
## 메모리: 157840 KB, 시간: 880 ms
from bisect import bisect_left
n = int(input())
arr = tuple(map(int, input().split()))
result = [arr[0]]

for i in arr:
    if result[-1] < i:
        result.append(i)
        
    else: # result[-1] >= i
        result[bisect_left(result, i)] = i

print(len(result))