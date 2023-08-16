import sys
input = sys.stdin.readline

k,n = map(int,input().split())
lines = [int(input()) for _ in range(k)]

def binary_search():
    st = 1
    en = max(lines)
    while st<=en:
        mid=(st+en)//2
        cnt=0
        for line in lines:
            if line>=mid:
                cnt+=line//mid
        
        if cnt<n:
            en=mid-1
        else:
            st=mid+1
    return en

print(binary_search())
            
#메모리 31256kb 시간 476ms >> 그냥 input
#메모리 31256kb 시간 76ms >>readline