'''
# 백준_2343_기타 레슨. 실버 1. 풀이: 23.08.16 -> 실패

# How to  
- 블루레이 길이
    - 최소: 1개, 
    - 최대: n-m+1개
- 즉, 블루레이당 크기는 
    - 최소: 배열에서 가장 큰 값(arr[-1]), 
    - 최대: n-m+1개를 묶어서 더한 값(=sum(arr[:n-m+1]))
    

- 맨 앞에서부터 묶이는 블루레이의 최대 길이: n-m+1개
- 맨 뒤에서부터 묶이는 블루레이의 최대 길이: n // m

n2 = n - (n//3) = 6
n3 = n2 - (n2//2) = 3

# Review
- 풀이 시간:
- 아예 구상이 되지 않는다. 
- 어떤걸 이분탐색해야할지 모르겠다. 즉 블루레이 길이를 잡아야하나? 그럼 이때 mid는 무얼 의미하지? 모르겠다..
'''

# Code
# 1. 실패
## 메모리:  KB, 시간:  ms
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# answer_min, answer_max = arr[-1], sum(arr[:n-m+1])
# print(answer_min, answer_max)