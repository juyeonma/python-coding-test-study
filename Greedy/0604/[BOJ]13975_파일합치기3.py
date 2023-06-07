# 강의실 배정에서 배운 heapq 사용해보기..!
import sys
import heapq
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    file = [*map(int, input().split())]

    total = 0
    file.sort()
    while file:
        s = 0
        if len(file) >= 2:
            for i in range(2):
                s += heapq.heappop(file)
            heapq.heappush(file, s)
            total += s
        else:
            s = heapq.heappop(file)
    print(total)

# 메모리 : 152736KB	시간 : 5004ms
# 힙큐인데.. 왜.. 시간이 이렇게..크지..ㅠㅠ..
# 파이썬 자체가 ㅎㅎ.. 시간을 많이 사용하는 문제였다..
# 근데 while문 안에 for문을 또 돌려서 좀 더 속도가 늦었던 것 같다
# while len(file) > 1: 조건으로 하고 마지막것만 더해줬으면 빨랐을 것 같다..