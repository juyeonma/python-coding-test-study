n,k = map(int, input().split())

s=list(map(int,input().split()))
d = list(map(int, input().split()))


for i in range(k):
    p=[0]*(n)
    for j in range (n):
        p[d[j]-1]=s[j] 
    s=p
        
print(*s) #앞에 *을 붙이면 원소만 나올수 있음(리스트형태 말고)