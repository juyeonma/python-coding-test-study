'''
# 백준_14003_가장 긴 증가하는 부분 수열 5. 플레 5. 풀이: 23.08.10

## LIS: 최장 증가 부분 수열을 이용한 문제들
- DP로 풀면, 시간복잡도가 크다: O(n^2)
- 따라서 시간복잡도를 개선하기 위해 이분 탐색을 활용해야한다: O(nlogn)
- 백준에서는 입력의 최댓값에 따라 유형이 나뉜다.
    - dp: 11053, 14002, 11054, 11055, 11722
    - 이분탐색: 12015, 12738, 14003
-> dp와 이분탐색의 두 방법으로 풀어보자

# How to
- 길이 뿐 아니라 수열 그 자체를 구해야하는 문제로, 이전 문제들과 해답은 같다.
- 즉, 우선 이분탐색으로 정답 길이 k 및 원소별 LIS 길이를 구한다.
- k부터 거꾸로 탐색하면서 원소별 LIS 길이가 k와 같은 수를 정답에 기록

# Review
- 풀이 시간: 2시간
- 이전 풀이와 같이 해서 바로 맞추긴 했지만, 혹시 시간을 단축시킬 방법이 있나해서 여러가지 시도를 해봤다.
- 그러나.. 딱히 더 효율적인 풀이는 없는 듯 하다.
'''

# Code
# 1. 이분탐색: 성공
## 메모리: 211520 KB, 시간: 1236 ms
from bisect import bisect_left
n = int(input())
arr = tuple(map(int, input().split()))

result = [arr[0]]
cnt = [1] * n
answer = []
# result의 길이 = k, 즉 정답이 되는 최대 LIS 길이
# cnt: 원소별 LIS의 길이를 기록
for i, v in enumerate(arr):
    if result[-1] < v:
        result.append(v)
        cnt[i] += len(result) - 1
    else: # result[-1] >= v
        idx = bisect_left(result, v)
        result[idx] = v
        cnt[i] += idx

# 정답 k 출력하고,
k = len(result)
print(k)

# answer: LIS 수열.
idx = cnt.index(k)
answer = [0] * k
answer[-1] = str(arr[idx])
k -= 1

# k-1부터 k-2, k-3.. 1까지 거꾸로 탐색하기.
# 원소별 LIS 길이가 k와 같다면, 정답에 추가
for i in range(idx-1, -1, -1):
    if k == 0:
        break
    if cnt[i] == k:
        # 인덱스 겸 그 다음 수를 탐색하기 위해, k = k-1
        k -= 1
        # index는 0부터 시작이므로, k-1 인덱스에 k번째 수를 넣음
        answer[k] = str(arr[i])

print(' '.join(answer))


# 2. 실패 -> 경우의 수를 다 구해야해서..
# from bisect import bisect_left

# n = int(input())
# arr = tuple(map(int, input().split()))

# tmp = [arr[0]]
# dic = {}
# for i in arr:
#     if tmp[-1] < i:
#         tmp.append(i)
#     else: # tmp[-1] >= i
#         idx = bisect_left(tmp, i)
#         if tmp[idx] != i:
#             dic.setdefault(len(tmp), []).append(tmp)
#             tmp = tmp[:idx+1]
#             tmp[idx] = i
            
# dic.setdefault(len(tmp), []).append(tmp)

# answer = max(dic)
# print(answer)
# print(*dic[answer][0])