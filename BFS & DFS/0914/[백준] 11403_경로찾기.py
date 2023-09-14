n = int(input())
arr = {}
result = [[0]*n for _ in range(n)]

for i in range(n):
    temp=list(map(int,input().split()))
    arr[i]=[]
    for j in range(len(temp)):
        if temp[j]:
            arr[i].append(j)
q = []
for i in range(n):
    q.append(i)
    while q:
        cur_num=q.pop()
        for num in arr[cur_num]:
            if not result[i][num]:
                q.append(num)
                result[i][num]=1
                
for i in range(n):
    print(*result[i])

#메모리 31388 시간 68