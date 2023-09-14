'''
# 백준_2343_기타 레슨. 실버 1. 풀이: 23.08.16 -> 실패 -> 성공

# How to  
- 블루레이 길이
    - 최소: 1개, 
    - 최대: n-m+1개
- 즉, 블루레이당 크기는 
    - 최소: 배열에서 가장 큰 값(max(arr)), 
    - 최대: n-m+1개를 묶어서 더한 값(=sum(arr[:n-m+1]))

# Review
- 풀이 시간:
- 아예 구상이 되지 않는다. 
- 어떤걸 이분탐색해야할지 모르겠다. 즉 블루레이 길이를 잡아야하나? 그럼 이때 mid는 무얼 의미하지? 모르겠다..

- 답을 찾아보지 않으려 했으나, 이후 이분탐색 문제를 풀기위해 찾아보았다.
    - 출처: https://withthemilkyway.tistory.com/28
- 핵심은 "무얼 탐색할 것인가?" 였다.
    - 이 문제에서는 mid가 곧 블루레이의 크기였다.
    - 따라서 start, end는 블루레이 크기의 최솟값, 최댓값이 된다.
- 앞으로 이분탐색에서는 'What'에 더 집중해야겠다.

- 그런데, 맞힌 사람 풀이를 보니 이분탐색에서 bisect 라이브러리까지 더해서 더욱 빠르게 풀고있다.
    - 아직 코드가 잘 이해가 가지 않는다ㅠ
- 또, start <= end 냐, 아니면 start < end냐에 따라 end 갱신이 조금 달라진다.
- 아직..이분탐색은 너무 어렵다. 우선 기본적인 풀이대로 풀어보고, 나중에 응용하면서 시간을 단축해야겠다.
'''

# Code
# 1. 풀이 찾아봄
## 메모리: 42340 KB, 시간: 228 ms
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 블루레이 크기: 최소 max(arr) ~ 최대 sum(arr)

# 블루레이의 크기 찾기
def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt, tmp = 1, 0
        for i in arr:
            # 크기를 초과했다면, count 및 초기화
            if tmp + i > mid:
                cnt += 1
                tmp = 0
            tmp += i    

        # 같거나 더 많이 담았다 -> 블루레이 크기를 줄여보자
        if cnt <= m:
            end = mid - 1
            answer = mid
            
        # 더 적게 담았다 -> 블루레이 크기를 키우자
        else: # cnt > m
            start = mid + 1
            
    return answer
        
print(binary_search(max(arr), sum(arr[:n-m+1])))
