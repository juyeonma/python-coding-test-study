# sys로 풀지 않으면 시간초과
# 질투심은 한 보석의 최대개수를 넘을 수 없기때문에 탐색할 범위의 최대값으로 설정
# for문을 돌면서 나누어 줄수 있는 사람의 최대값을 센다 
# 최대값이 n보다 크면 질투심을 증가 시키고 작으면 감소시키는 방식으로 푼다.

import math,sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = [int(input()) for _ in range(m)]

def binary_search():
    st=1
    en=max(nums)
    while st<=en:
        mid=(st+en)//2
        cnt=0
        for num in nums:
            cnt+=math.ceil(num/mid)
        
        if cnt>n:
            st=mid+1
        else:
            en=mid-1
    return st

print(binary_search())

#메모리 45136kb 시간 808ms