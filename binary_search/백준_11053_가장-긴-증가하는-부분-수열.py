'''
# 백준_11053_가장 긴 증가하는 부분 수열. 실버 2. 풀이: 23.08.11

## LIS: 최장 증가 부분 수열을 이용한 문제들
- DP로 풀면, 시간복잡도가 크다: O(n^2)
- 따라서 시간복잡도를 개선하기 위해 이분 탐색을 활용해야한다: O(nlogn)
- 백준에서는 입력의 최댓값에 따라 유형이 나뉜다.
    - dp: 11053, 14002, 11054, 11055, 11722
    - 이분탐색: 12015, 12738, 14003
-> dp와 이분탐색의 두 방법으로 풀어보자

# How to
- LIS의 길이를 구하는 문제이기 때문에, bisect로 길이를 구하는게 가장 빠르다.
    - 우선 dp에 배열의 첫번째 원소를 넣어서 초기화한다.
    - 원래 배열의 원소가 dp의 어느 원소 다음에 위치해야하는지를 구해서 넣는다.


# Review
- 풀이 시간: 1시간
- 먼저 이분탐색과 bisect 라이브러리 공부를 했다.
- 이분탐색으로 풀 때, 길이를 구하는건 bisect를 사용하거나 직접 함수를 구현하면 되어서 쉽다.
- 그런데.. 이분탐색으로 원소까지 정확히 구하는건 너무 어려울 듯 하다..
'''

# Code
# 1. DP
## 메모리: 31256 KB, 시간: 160 ms
n = int(input())
arr = tuple(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+1, dp[i])
            
print(max(dp))


# 2. 이분 탐색: 길이만 구하기
## 메모리: 33320 KB, 시간: 44 ms
from bisect import bisect_left
n = int(input())
arr = tuple(map(int, input().split()))
dp = [arr[0]]

''' 
# 직접 구현한다면: 31256 KB
def bisect_left(arr, x, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else: # arr[mid] >= x
            hi = mid
            
    return lo
'''
    
for i in arr:
    if dp[-1] < i:
        dp.append(i)
    else: # dp[-1] >= i
        idx = bisect_left(dp, i, 0, len(dp))
        dp[idx] = i

print(len(dp))
