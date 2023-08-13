'''
# 백준_12015_가장 긴 증가하는 부분 수열 2. 골드 2. 풀이: 23.08.13

## LIS: 최장 증가 부분 수열을 이용한 문제들
- DP로 풀면, 시간복잡도가 크다: O(n^2)
- 따라서 시간복잡도를 개선하기 위해 이분 탐색을 활용해야한다: O(nlogn)
- 백준에서는 입력의 최댓값에 따라 유형이 나뉜다.
    - dp: 11053, 14002, 11054, 11055, 11722
    - 이분탐색: 12015, 12738, 14003
-> dp와 이분탐색의 두 방법으로 풀어보자

# How to
- 입력값이 1,000,000로 매우 크다. -> 이분탐색 사용
- 길이를 구하는 문제이므로 bisect_left를 사용한다.
    - 11053 문제와 같다.
    - 배열의 첫번째 원소로 dp를 초기화.
    - 매번 현재 원소가 dp의 어느 위치에 들어갈지 구하고, 삽입.
    
## 반례

# Review
- 풀이 시간: 5분
'''

# Code
# 1. DP: 시간초과
## 메모리:  KB, 시간:  ms
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# 2. 이분탐색 bisect 사용: 
## 메모리: 157640 KB, 시간: 956 ms
from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
result = [arr[0]]

for i in arr:
    if result[-1] < i:
        result.append(i)
        
    else: # result[-1] >= i
        idx = bisect_left(result, i, lo=0, hi=len(result))
        result[idx] = i
        
print(len(result))
