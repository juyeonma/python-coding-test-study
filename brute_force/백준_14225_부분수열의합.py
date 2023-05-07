#[백준] 14225 - 부분수열의 합 
n = int(input())
num = list(map(int,input().split()))
visited = [0]*10000000

def dfs(idx,sum) :
    if idx == n :
       return
    sum += num[idx]
    visited[sum] = 1
    dfs(idx+1, sum)
    dfs(idx+1, sum-num[idx])

dfs(0,0)
print(visited[1:].index(0)+1)