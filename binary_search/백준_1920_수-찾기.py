'''
# 백준_1920_수-찾기. 실버 4. 풀이: 23.08.09

# How to

## 1. 이분탐색
- 전형적인 이분탐색 코드 구현
    - 타겟을 찾으면, 1
    - start > end가 되었다면, 타겟을 못 찾은 것이므로, 0

## 2. set 사용
- 목록을 set으로 입력 받아서, 타겟이 목록에 있는지 탐색.

# Review
- 풀이 시간: 20분
- 분명히 코드에 이상이 없는데 왜 틀리지, 하고 다시보니까 조건에 "모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다."였다..
    - 조건을 꼼꼼히 살피자ㅠㅠ
'''

# Code
# 1. 이분탐색 사용: 성공
## 메모리: 47268 KB, 시간: 476 ms
import sys
input = sys.stdin.readline

n = int(input())
arr_n = list(map(int, input().split()))
arr_n.sort()

m = int(input())
arr_m = tuple(map(int, input().split()))

def binary_search(num, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        # num을 찾았다면, 성공
        if arr_n[mid] == num:
            return 1
        
        # 너무 수가 크다면, 더 작은 수(왼쪽)로 범위 좁히기
        elif arr_n[mid] > num:
            end = mid - 1
        
        # 너무 수가 작다면, 더 큰 수(오른쪽)로 범위 좁히기
        else: # arr_n[mid] < num
            start = mid + 1
            
    # start > end가 되었는데도 num을 찾지 못했다면, 실패
    return 0

for num in arr_m:
    print(binary_search(num, 0, n-1))
    

# 2. set 사용: 성공
## 메모리: 50408 KB, 시간: 180 ms
import sys
input = sys.stdin.readline

n = int(input())
arr_n = set(map(int, input().split()))

m = int(input())
arr_m = list(map(int, input().split()))

for i in arr_m:
    if i in arr_n:
        print(1)
    else:
        print(0)
