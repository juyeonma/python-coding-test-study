# n,m = map(int,input().split())
# arr = [False]*m
# isused = [False]*(n+1)

# def func(k):
#     if k==m:
#         print(*arr)
#         return

#     for i in range(1,n+1):
#         if not isused[i]:
#             arr[k]=i
#             isused[i]=True
#             func(k+1)
#             isused[i]=False

# func(0)

n,m = map(int,input().split())
arr = [False]*m
isused = [False]*(n+1)

def func(k):
    if k==m:
        print(*arr)
        return
    
    for i in range(1,n+1):
        if not isused[i]:
            arr[k]=i
            isused[i]=True
            func(k+1)
            isused[i]=False

func(0)