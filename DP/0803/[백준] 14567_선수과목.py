#튜플이 리스트보다 속도가 빠르다. 데이터를 추가하거나 삭제하느 경우가 없을땐 튜플을 사용하는 게 좋다
# 위상정렬 문제라는 데 위상정렬을 사용하지 않아서 시간이 길게 나온건가?

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d = [1]*(n+1)
nums = [tuple(map(int,input().split())) for _ in range(m)]
# nums = [list(map(int,input().split())) for _ in range(m)]
nums.sort()
for a,b in nums:
    if d[b]<=1+d[a]:
        d[b]=1+d[a]

print(*d[1:])

#메모리 163868kb 시간 : 1956ms  주석처리 된 것으로 했을 때
#메모리 93548kb 시간 : 1344ms  튜플로 했을떄