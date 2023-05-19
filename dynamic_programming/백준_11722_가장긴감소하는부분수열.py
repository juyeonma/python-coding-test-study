n = int(input())
a = list(map(int, input().split()))

d=[1]*n

for i in range(1,n):
    for j in range(i):
        if a[j]>a[i]: #자신보다 앞쪽에있는 숫자가 크다면
            d[i]=max(d[i],d[j]+1) #자기 자신과 앞쪽 숫자에서 1을 더한 값을 비교해서 큰값 저장
            
print(max(d))

# 코드길이 : 189 B
# 시간 : 148 ms
# 메모리 : 31256 KB