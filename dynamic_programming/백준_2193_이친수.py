n = int(input())

d = [0]*90 #90개로 범위를 한정지어줘야 정답처리가 됐다

d[0]=1
d[1]=1

# n=i일때, 이친수의 값은 i-2일때와 i-1일때의 값을 합하면 됐음
for i in range(2,n):
    d[i]=d[i-1]+d[i-2]
print(d[n-1])

# 코드길이 : 102 B
# 시간 : 40 ms
# 메모리 : 31256 KB