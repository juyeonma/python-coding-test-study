#완탐이나 그리디를 생각햇는데 이 문제는 dp인걸 알아서 시도를 하지는 않았다.
#dp로 풀 방법이 생각이 안나서 일고리즘을 봤는데 배낭문제라고 나와있었다.

c,n = map(int,input().split())
arr= [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[1])
dp = [[0]*(n+1) for _ in range(c+1)]

for i in range(1,n+1):
    for j in range(1,c+1):
        if arr[i][1]<=j:
            arr[i-1][1],arr[i]