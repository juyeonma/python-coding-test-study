'''
# 백준_3020_개똥벌레. 골드 5. 풀이: 23.08.16 -> 실패

# How to  
- 석순: 아래서부터. 종유석: 위에서부터.
- 석순, 종유석, 석순, 종유석.. 반복

# Review
- 풀이 시간:
- 문제는 정답에서 장애물의 개수도 세야한다는 점이다.
- 그런데 이분탐색은 점점 범위를 좁히다보니, 이미 세어본 mid값은 다시 안 가게 될텐데..이걸 어떻게 해결해야할지 모르겠다.
'''

# Code
# 1. 이분탐색: 실패
## 메모리:  KB, 시간:  ms
import sys
input = sys.stdin.readline

n, h = map(int, input().split())
up_arr, down_arr = [0] * (h+1), [0] * (h+1)
for i in range(n):
    now = int(input())
    if i % 2: # 홀수 => 종유석
        up_arr[now] += 1
    else: # 짝수 => 석순
        down_arr[now] += 1
        
answer = [0] * h

def binary_search(start=0, end=h+1):
    while start < end:
        mid = (start + end) // 2
        
        # down을 기준으로..
        # 석순과 종유석 장애물 개수를 구하고, 기록
        cnt_down = sum(down_arr[mid:])
        cnt_up = sum(up_arr[-mid:])        
        cnt = cnt_down + cnt_up
        answer[cnt] += 1

        # 종유석이 더 많으면, 석순 쪽으로 내려간다.
        if cnt_down <= cnt_up:
            end = mid - 1
            
        # 석순이 더 많으면, 종유석 쪽으로 올라간다.
        else: # cnt_down > cnt_up
            start = mid + 1
            
    return cnt, answer[cnt]

print(binary_search(start=1, end=h))


# 2. 시간초과
## 메모리:  KB, 시간:  ms
import sys
input = sys.stdin.readline

n, h = map(int, input().split())
up_arr, down_arr = [0] * (h+1), [0] * (h+1)
for i in range(n):
    now = int(input())
    if i % 2: # 홀수 => 종유석
        up_arr[now] += 1
    else: # 짝수 => 석순
        down_arr[now] += 1
        
# 높이별로 장애물 개수 저장
answer = [0] * h
for i in range(1, h+1):
    answer[i-1]=(sum(down_arr[i:]) + sum(up_arr[-i:]))

result = min(answer)
print(result, answer.count(result))