# 투 포인터 풀이
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
def check():
    st=0
    en=len(nums)-1
    min_s=2e9
    st_num=0
    en_num=0
    while st<en:
      s=nums[st]+nums[en]
      if min_s>abs(s):
          st_num=nums[st]
          en_num=nums[en]
          min_s=abs(s)
      if s<0:
          st+=1
      elif s>0:
          en-=1
      else:
          return (st_num,en_num)
    return (st_num,en_num)

print(*check())



# 이분탐색 풀이
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
def binary_search(min_v,left,right,st):
    en = n-1
    cur_i = st
    st+=1
    while st<=en:
        mid=(st+en)//2
        tmp = nums[cur_i]+nums[mid]
        if abs(tmp)<min_v:
            min_v = abs(tmp)
            left = cur_i
            right = mid
        if tmp<0:
            st=mid+1
        elif tmp>0:
            en=mid-1
        else:
            return 0,cur_i,mid
    return min_v,left,right

tmp = 2e9
left = 0
right = 0
for i in range(n-1):
    tmp,left,right = binary_search(tmp,left,right,i)
print(nums[left],nums[right])