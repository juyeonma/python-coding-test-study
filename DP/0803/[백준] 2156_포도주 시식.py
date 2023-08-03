# sys사용하니까 시간이 엄청나게 줄었다..

# 첫 번째 풀이는 d[n]은 무조건 해당 위치의 포도주를 먹는상태에서의 최대값을 구하는 것이다
# 그러므로 n 위치의 포도주를 먹고 n-1포도주를 먹고 n-2는 먹지 않는 것
# n 위치의 포도주를 먹고 n-1포도주를 먹지 않고 n-2까지의 포도주 최대값
# n 위치의 포도주를 먹고 n-1,n-2를 먹지 않고, n-3까지의 포도주 최대값
# 중에서 최대값을 구하면 된다

# 두 번째 풀이는 d[n]에서 n번째 포도주를 먹든 말든 신경쓰지 않고 최대값을 구하는 것이다.
# 그러므로 n번째를 먹었을 때, n-1을 먹고 n-2는 먹지 않고 n-3까지의 최대값
# n번째를 먹고, n-1을 먹지않고, n-2까지의 최대값
# n번째를 먹지 않고, n-1까지의 최대값
# 중에서 최대값을 구한다

import sys
input = sys.stdin.readline;

n = int(input())
nums = [0]+[int(input()) for _ in range(n)]
d=[[0,0] for _ in range(n+1)]

d[1]=[nums[1],nums[1]]
if n>1:
    d[2][0] = nums[2]
    d[2][1] = nums[2] + nums[1] 

for i in range (3,n+1):
    d[i][0] = nums[i] + max(*d[i-2],*d[i-3])
    d[i][1] = nums[i] + d[i-1][0]

print(max(*d[n],*d[n-1]))

#메모리 32276kb 시간 60ms


import sys
input = sys.stdin.readline;

n = int(input())
nums = [0] + [int(input()) for _ in range(n)]
d = [0]*(n+1)
d[1] = nums[1]
if n>1:
    d[2] = nums[1] + nums[2]
if n>2:
    d[3] = max(nums[3]+nums[1],nums[3]+nums[2],d[2])

for i in range(4,n+1):
    d[i] = max(nums[i]+nums[i-1]+d[i-3],nums[i]+d[i-2],d[i-1])

print(d[n])
#메모리 31256kb 시간 52ms