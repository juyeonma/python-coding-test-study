from collections import defaultdict

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
m = int(input())
cards = list(map(int,input().split()))

check = defaultdict(int)
for i in nums:
    check[i]+=1

def binary_search(i):
    st = 0
    en = n-1
    while st<=en:
        mid=(st+en)//2
        if nums[mid]<i:
            st=mid+1
        elif nums[mid]>i:
            en=mid-1
        else:
            return check[i]
    
    return 0

for i in cards:
    print(binary_search(i),end=" ")

#메모리 115008kb 시간 2800ms