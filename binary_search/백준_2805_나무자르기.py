'''
# 백준_2805_나무자르기. 실버 2. 풀이: 23.08.09

# How to
- 매번 mid에서 나무를 잘랐을 때 길이를 구해서 비교한다.

# Review
- 풀이 시간: 30분
- 이코테에서 봤던 문제인데도, 조금 헷갈렸다.
- 그런데 랜선자르기 문제를 풀고나니, 이 문제도 m == cnt 일 때도 start = mid + 1 로 갱신하는게 더 정확한 풀이같다.
'''

# Code
# 1. 성공
## 메모리: 150336 KB, 시간: 2448 ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = tuple(map(int, input().split()))

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in tree:
            if i > mid:
                cnt += i - mid
                
        # 알맞게 잘랐다면, return
        if m == cnt:
            return mid
        
        # 너무 적게 잘랐다면, 더 자른다
        elif m > cnt:
            end = mid - 1
        
        # 너무 많이 잘랐다면, 덜 자른다
        else:
            start = mid + 1
        
    return end

print(binary_search(0, max(tree)))