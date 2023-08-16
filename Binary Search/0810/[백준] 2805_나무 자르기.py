n,m = map(int,input().split())
nums = list(map(int,input().split()))

def binary_search():
    st = 0
    en = max(nums)

    while st<=en:
        mid=(st+en)//2
        length=0
        for num in nums:
            if mid<num:
                length+=num-mid
        if length<m:
            en=mid-1
        else:
            st=mid+1
    return en

print(binary_search())

#메모리 150336kb 시간 2176ms