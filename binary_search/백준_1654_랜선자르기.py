'''
# 백준_1654_랜선자르기. 실버 2. 풀이: 23.08.09 -> 실패

# How to
- 자꾸 틀려서 반례를 찾아보니, "N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다." 조건이 중요했다.
    - 즉, 나머지는 버리기 때문에, 같은 개수의 랜선이여도 더 길게 자를 수 있다.
- 그리고 k <= n 이라서 무조건 랜선을 잘라야하고, 분모가 0이 되면 안되기도 해서 start = 1로 초기화 해야한다.


## 반례
"N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다."  
1 3
30
정답: 10

- 만약 cnt == n일 때 바로 return 하면,
    (start, end, min = 8, 10, 9)일 때 cnt = 3이 되어 바로 9가 답이된다.
- 그러나, cnt == n 이어도 start = mid + 1 로 갱신하여 진행하며,
    (start, end, min) = (10, 10, 10)일 때 cnt = 3, 즉 10이 정답이다.

# Review
- 풀이 시간:
- 맞힌 사람 풀이를 보니, end 값을 max(arr)이 아니라 sum(arr) // n 으로 하는걸 발견했다.
    - 즉 어짜피 랜선을 잘라야 하기 때문에, 최댓값이 sum(arr) // n 으로 하나보다.
'''

# Code
# 1. 맞힌 사람 코드
## 메모리: 31256 KB, 시간: 60 ms
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = tuple(int(input()) for _ in range(k))

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        
        cnt = 0
        for i in arr:
            cnt += i // mid
        
        # 너무 길게 잘라서 개수가 부족할 때, 더 짧게 자르기
        if cnt < n:
            end = mid - 1
            
        # 너무 짧게 잘라서 개수가 같거나 넘칠 때, 더 길게 자르기
        else: # cnt >= n
            start = mid + 1
            
    return end

print(binary_search(1, max(arr)))
