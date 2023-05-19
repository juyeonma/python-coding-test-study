n = int(input())

d = [0]*(n+1)

for i in range(2,n+1): #d[1]은 1이되는데 필요한 횟수가 0이므로 2부터 시작
    d[i]=d[i-1]+1 #i가 1이 되는데 걸리는 최소 횟수 초기화
    if i%3 ==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%2==0:
        d[i]=min(d[i], d[i//2]+1)

print(d[n])

# 코드길이 : 308 B
# 시간 : 544 ms
# 메모리 : 39068 KB