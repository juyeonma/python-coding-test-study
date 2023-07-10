# n과 m 시리즈 문제 중 하나와 같다. 
# 거기서 매번 합을 확인하며 카운팅만 하면 된다

n,s = map(int,input().split())
nums = list(map(int,input().split()))
count=0
arr = []
def dfs(k):
    global count

    for i in range(k,n):
        arr.append(nums[i])
        if sum(arr)==s:
            count+=1
        dfs(i+1)
        arr.pop()

dfs(0)
print(count)

#17분
#메모리 : 31256kb 시간 : 464ms
