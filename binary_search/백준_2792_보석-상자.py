'''
# 백준_2792_보석 상자. 실버 1. 풀이: 23.08.16

# How to
- 정답의 최댓값은 곧 보석 중 최대로 많은 개수.
- 모든 보석을 mid 개씩 나누면, 때, 몇명이 받게 되나?
    - 보석을 받은 수 <= 학생 수라면,
        - 나누어주는 보석 수를 줄인다: end = mid
    - 보석을 받은 수 > 학생 수라면,
        - 나누어주는 보석 수를 늘린다: start = mid + 1
- start == end 가 되면, end를 return 한다. -> 이게 곧 정답


## 예제
학생 7명, 보석 5개일 때, 보석 배열: 7, 1, 7, 4, 4

start, end: 1, 7 -> mid: 4
4개씩 나누면, 총 7명

start, end: 1, 4 -> mid: 2
2개씩 나누면, 총 13명

start, end: 3, 4 -> mid: 3
3개씩 나누면, 총 11명

start, end: 4, 4 -> start == end 이므로, return 4 


# Review
- 풀이 시간: 30분
- 이분탐색을 '보석'에 맞추어야 할지, '학생 수'에 맞추어야 할지 고민했다.
- 그러다가 mid 값이 곧 나누는 보석의 단위라고 생각하니, 예제가 술술 풀렸다.
- 이분탐색에서는 start, end, mid가 어떤걸 의미하는지를 빨리 파악하는게 관건인듯 하다.
'''

# Code
# 1.
## 메모리: 43012 KB, 시간: 1120 ms
import sys
input = sys.stdin.readline

# n: 학생 수, m: 보석 수
n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

def binary_search(student, start, end):
    while start < end:
        # 모든 보석을 mid 개씩 나누면, 때, 몇명이 받게 되나?
        mid = (start + end) // 2
        
        # 보석을 받는 사람은 몇명?
        cnt = 0
        for i in arr:
            # 몫과 나머지 유무(나머지가 존재하면 1, 없으면 0)를 더함.
            cnt += i // mid + (i % mid != 0)

        # 보석을 받은 수가 학생 수와 같거나 적을 경우, 나누어주는 보석 개수를 줄인다.
        # 마지막에 end가 곧 정답이므로, mid - 1이 아니라 mid로 갱신한다.
        if cnt <= student:
            end = mid
        
        # 보석을 받은 수가 학생 수보다 많을 경우, 나누어주는 보석 개수를 늘린다.
        else: # cnt > student:
            start = mid + 1
            
    # start == end가 되면, end를 return
    return end

print(binary_search(n, 1, max(arr)))