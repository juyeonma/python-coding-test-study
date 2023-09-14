'''
# 백준_1477_휴게소 세우기. 골드 4. 풀이: 23.08.21 -> 실패 -> 다시 풀기

# How to

## 반례

# Review
- 풀이 시간:
'''

# Code
# 1. 실패
## 메모리:  KB, 시간:  ms
# 현재 n개, 앞으로 m개 더 , 고속도로 길이 l
n, m, l = map(int, input().split())
arr = list(map(int, input().split()))

answer = max(arr[0], l - arr[-1])
for i in range(n-1):
    answer = max(answer, arr[i+1] - arr[i])
    
    
def binary_search(target, start, end, cnt):
    while start < end and cnt:
        mid = (start + end) // 2
        
        tmp = arr[mid] - arr[start]
        
        if tmp < target:
            start = mid
            cnt -= 1
            target = tmp
            
        else: # tmp >= tartget
            end = mid - 1
            
    return target
            

# end의 범위를 늘려간다.
for end in range(n):
    answer = min(answer, binary_search(answer, 0, end, m))
    
print(answer)