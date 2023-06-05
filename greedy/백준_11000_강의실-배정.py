'''
# 백준_11000_강의실 배정. 골드 5. 풀이: 23.05.31 -> 실패

# How to
1. 우선 순위 큐 사용(정석 풀이?):
- 강의 목록을 순차적으로 탐색하며, 현재 최소 종료시간과 비교
    - 현재 회의실 종료시간 <= 다음 회의 시작시간이면, 현재 종료시간을 큐에서 제거
    - 조건에 맞는지 여부와 상관없이 다음 회의 종료시간을 큐에 추가
- 모든 강의를 탐색한 이후에 큐에 남는건 각 강의실의 마지막 수업들.
- 따라서 큐의 길이 = 강의실 갯수
    
2. 시작시간을 탐색하며 종료시간과 비교(더 빠름):
- 시작과 종료시간을 각긱 list에 담고, 오름차순 정렬
- 회의실 최댓값은 곧 강의 갯수(=n)
- 시작시간을 순차적으로 탐색
    - 만약 종료 시간 <= 시작 시간이면, 종료시간 index 1 증가하고, 회의실 갯수 1 감소


# Review
- 회의실 사용.. 예전에도 틀렸는데, 또 틀렸다. 정렬을 해야한다는건 기억났지만..
- 찾아보니, 우선 순위 큐가 정석 풀이 같다.
    - 그러나 시작시간을 탐색하며 종료시간과 비교하는게 훨씬 더 빠르고 메모리도 작다.
- 결국 핵심은  종료 시간 <= 시작 시간인 경우 회의실 갯수가 줄어든다는 것
    - 1.에서는 이 경우 큐에서 제거했고, 2.에서는 회의실 갯수를 1 감소했다.
'''


# 1. 시간초과 Code
n = int(input())
arr = dict(map(lambda _: map(int, input().split()), range(n)))
m = max(arr)
sort_key = sorted(arr)

i = sort_key[0]
cnt = 0
while arr:
    tmp = arr[i]
    del arr[i]
    sort_key.remove(i)
    for j in range(tmp, m+1):
        if j in arr:
            i = j
            break
    else:
        cnt += 1
        if sort_key:
            i = sort_key[0]
        else:
            print(cnt)
            
            
# 모범답안 Code
# 1. 우선 순위 큐 사용: 73584 KB 392 ms
import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

q = []
heapq.heappush(q, arr[0][1])

for i in range(1, n):
    # 현재 회의실 종료 시간 <= 다음 회의 시작 시간
    # 이어서 회의실 사용 가능
    if q[0] <= arr[i][0]:
        heapq.heappop(q)
    heapq.heappush(q, arr[i][1])

print(len(q))


# 2. 시작시간을 탐색하며 종료시간과 비교: 46716 KB 256 ms
import sys
input = sys.stdin.readline

n = int(input())

# zip을 사용하면, 메모리와 시간이 크게 증가: 135808 KB 576 ms
# start, end = map(list, zip(*[map(int, input().split()) for _ in range(n)]))
start, end = [], []
for _ in range(n):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)
    
# 시작시간을 순차적으로 탐색하기 때문에, 오름차순 정렬
# 만약 종료시간을 탐색하면서 조건에 맞을 시 시작시간 index를 증가시킨다면(즉 시작시간은 전체를 탐색하지 않음)
# 내림차순 정렬 및 탐색을 end로 하면 됨.
start.sort()
end.sort()

e = 0
for s in start:
    # 종료 시간 <= 시작 시간이면, 
    if end[e] <= s:
        e += 1
        n -= 1
print(n)
            

'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''