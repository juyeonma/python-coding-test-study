n = int(input())
nums = list(map(int,input().split()))
nums.sort()
m = int(input())
check = list(map(int,input().split()))

def binary_search(i):
    st = 0
    en = n-1
    while st<=en:
      mid=(st+en)//2
      if nums[mid]<=i:
        st=mid+1
      else: 
        en=mid-1
    
    if nums[en]==i:
      return 1
    else:
      return 0

for i in check:
    print(binary_search(i))

#메모리 46732kb 시간 436ms