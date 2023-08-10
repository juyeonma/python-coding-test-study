'''
# 백준_10816_숫자 카드 2. 실버 4. 풀이: 23.08.09 -> 실패

# How to
## bisect 라이브러리 설명
- target의 범위가 [start:end]일 때, start(즉 low)와 end(즉 high)를 찾는다.
- 각각 종료 조건은 low < high 가 아닌 순간, 즉 low == high가 되면 low 값을 return 한다.
- 그런데 기본적인 이분탐색에서는 mid에서 +- 1씩 갱신하지만, bisect는 다르다.

## bisect_left:
- low: target & 낮은 인덱스(left) 방향으로 범위를 좁힌다.
- target을 찾았을 때 high = mid로 갱신하면, 
    low == high가 되는 순간 반복문을 탈출하여, low == high == mid == target이 return 된다.

## bisect_right:
- high: target & 높은 인덱스(right) 방향으로 범위를 좁힌다.
- target을 찾았을 때 low = mid + 1로 갱신하면,
    low == high가 되는 순간 반복문을 탈출하여 low == target + 1가 return 된다.


## 딕셔너리에 key가 없을 때는 기본값을, key가 있을 때는 1 증가하는 방법 4가지
1) 그냥 조건문
dic = {}
for i in input().split():
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

2) 조건문
dic = {}
for i in input().split():
    if i not in dic:
        dic[i] = 0
    dic[i] += 1
    
3) setdefault
dic = {}
for i in input().split():
    dic.setdefault(i, 0) 
    dic[i] += 1
    
4) collections.defaultdict
from collections import defaultdict
dic = defaultdict(int)
for i in input().split():
    dic[i] += 1


# Review
- 풀이 시간:
- bisect 라이브러리를 써야한다는걸 알았지만, 함수도 기억나지 않고 구현도 실패했다.
    - start와 end, 즉 low와 high를 줄여나가는 부분이 어려웠다.
- 결국 검색해서 bisect 라이브러리 코드를 이해했고, 이를 구현했다.
- 그럼에도 불구하고 너무 느려서 맞힌 사람 코드를 보니, 이 문제가 이분탐색 유형임에도 불구하고 딕셔너리로 구현하는게 제일 빠른거였다. 
    - 이때 딕셔너리 설정시 collections.defaultdict 이나 setdefault 를 사용하면 더 간편하다는 것도 배웠다.
'''

# 실패 후 검색해서 구현한 Code
# 1. bisect 라이브러리
## 메모리: 120632 KB, 시간: 2132 ms
import bisect
import sys
input = sys.stdin.readline

n = int(input())
card = sorted(map(int, input().split()))

m = int(input())
num = tuple(map(int, input().split()))

dic = {}
answer = []

def binary_search(target):
    # 이미 구한 값이라면, 딕셔너리에서 찾아서 return
    if target in dic:
        return dic[target]
    
    # target의 범위: card[start:end] 를 찾으면 그 차이가 곧 답.
    start = bisect.bisect_left(card, target, lo=0, hi=n)
    end = bisect.bisect_right(card, target, lo=start, hi=n)
    
    dic[target] = end - start
    
    return end - start

for target in num:
    answer.append(binary_search(target))
    
print(*answer)

'''
## bisect를 직접 구현하면, 더 느리다: 118596 KB, 시간: 4104 ms
def bisect_left(target, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if card[mid] < target:
            lo = mid + 1
        else: # card[mid] >= target
            hi = mid 
    return lo

def bisect_right(target, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if card[mid] > target:
            hi = mid
        else: # card[mid] <= target
            lo = mid + 1
    return lo
'''


# 2. 딕셔너리에 저장
## 메모리: 159396 KB, 시간: 572 ms
## collections.defaultdict 사용하면: 153096 KB, 660 ms
## setdefault 사용하면: 153504 KB, 604 ms
import sys
input = sys.stdin.readline

n = int(input())
dic = {}
answer = []

for i in input().split():
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

m = int(input())
for j in input().split():
    if j in dic:
        answer.append(str(dic[j]))
    else:
        answer.append('0')
        
print(' '.join(answer))
