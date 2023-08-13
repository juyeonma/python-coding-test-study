'''
# 백준_14002_가장 긴 증가하는 부분 수열 4. 골드 4. 풀이: 23.08.13

## LIS: 최장 증가 부분 수열을 이용한 문제들
- DP로 풀면, 시간복잡도가 크다: O(n^2)
- 따라서 시간복잡도를 개선하기 위해 이분 탐색을 활용해야한다: O(nlogn)
- 백준에서는 입력의 최댓값에 따라 유형이 나뉜다.
    - dp: 11053, 14002, 11054, 11055, 11722
    - 이분탐색: 12015, 12738, 14003
-> dp와 이분탐색의 두 방법으로 풀어보자

# How to
- 입력의 범위가 크지 않고(1,000), 양수만 주어진다.
- LIS의 길이 뿐 아니라 수열 자체도 출력해야 한다.
- 따라서, 원소별 LIS 길이를 구하고, 거꾸로 탐색하면서 수열의 원소를 정답에 추가한다.

- 왜 거꾸로 탐색해야할까?
    - cnt: 원소별 LIS의 길이가 담긴 리스트.
    - i < j 일 때 cnt[i] == cnt[j] 라면, 무조건 arr[i] >= arr[j]
        - 만약 arr[i] < arr[j] 라면, 당연히 cnt[i] < cnt[j] 가 될테니까.
    - 따라서 뒤에서부터 cnt 거슬러 올라갈 때, cnt[i] == k 면 바로 정답에 추가해도 된다.


# Review
- 풀이 시간: 1시간
- 그전까지는 LIS의 길이만 찾았는데, 이번에는 수열 자체도 구해야했다.
    - 단순히 bisect로는 길이만 정확하게 구할 수 있기 때문에, 다시 공부하면서 코드를 돌려봤다.
- 결국 핵심은 원소별 LIS의 길이를 구하고 -> 이를 거꾸로 탐색해서 정답을 구하고 -> 다시 뒤집어서 출력하는 것이었다.
'''

# Code
# 1. DP
## 메모리: 31256 KB, 시간: 156 ms
n = int(input())
arr = tuple(map(int, input().split()))
dp = [1] * n

# 원소별 LIS의 길이를 찾고
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
# 최댓값부터 거꾸로 탐색하면서, 연속되는 값 찾기
idx = dp.index(max(dp))
k = max(dp) - 1
answer = [arr[idx]]
for i in range(idx-1, -1, -1):
    if dp[i] == k:
        answer.append(arr[i])
        k -= 1
    
print(max(dp))
# 거꾸로 탐색하며 찾았으므로, 뒤집어서 출력
print(*answer[::-1])


# 2. 이분탐색: bisect_left
## 메모리: 33320 KB, 시간: 44 ms
from bisect import bisect_left
n = int(input())
arr = tuple(map(int, input().split()))
result = [arr[0]]
cnt = [1] * n
answer = []

# result: LIS의 최대 길이를 찾기 위해서
# cnt: 원소별 LIS의 길이를 담음
for i in range(n):
    idx = bisect_left(result, arr[i])
    if result[-1] < arr[i]:
        result.append(arr[i])
    else: # result[-1] >= arr[i]
        result[idx] = arr[i]
    cnt[i] += idx

# cnt를 최댓값부터 거꾸로 탐색하면서, 연속되는 값 찾기
idx = cnt.index(len(result))
k = len(result) - 1
answer = [arr[idx]]
for i in range(idx-1, -1, -1):
    if cnt[i] == k:
        answer.append(arr[i])
        k -= 1     
'''
# while로 하면
i = idx-1
while k:
    if cnt[i] == k:
        answer.append(arr[i])
        k -= 1
    i -= 1
'''

print(len(result))
# 거꾸로 탐색하며 찾았으므로, 뒤집어서 출력
print(*answer[::-1])
