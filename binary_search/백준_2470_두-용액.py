'''
# 백준_2470_두 용액. 골드 5. 풀이: 23.08.17 -> 실패

# How to  
- 산성: 양수, 알칼리: 음수
- 그냥 값으로 정렬해보고, 절대값으로도 정렬해봤다.

# Review
- 풀이 시간:
- 왜 틀렸는지 모르겠다.. 우선 음수가 등장해서 정렬부터 막힌다. ㅠㅠ
- 반례를 넣으니 틀리는게 보이는데, 이걸 어떻게 수정해야할지 모르겠다. 
    - 반복문 탈출 조건을 start >= end로 하는게 맞나?
    - 갱신시에, end 를 m-1로 해야할지 mid로 해야할지 모르겠다.
'''

# Code
# 1. 실패
## 메모리:  KB, 시간:  ms
n = int(input())
arr_original = list(map(int, input().split()))

def binary_search(arr, start=0, end=n-1):
    before_start, before_end = start, end
    while start < end:
        tmp = 0
        mid = (start + end) // 2
        tmp = arr[start] + arr[end]

        before_start, before_end = start, end
        
        if tmp == 0:
            return arr[start], arr[end], tmp
        
        elif tmp < 0:
            start = mid + 1
        
        else: # tmp > 0
            end = mid - 1
    
    return sorted([arr[before_start], arr[before_end]])


arr_sort = sorted(arr_original)
arr_abs_sort = sorted(arr_original, key=abs)

if abs(arr_sort[-1] + arr_sort[-2]) < abs(arr_abs_sort[-1] + arr_abs_sort[-2]):
    print(*binary_search(arr_sort))
else:
    print(*binary_search(arr_abs_sort))
