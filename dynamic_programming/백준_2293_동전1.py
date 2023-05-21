n, k = map(int, input().split())
coin=[]
for _ in range(n):
    coin.append(int(input()))
    
d=[0]*(k+1) #인덱스가 동전의 합, 즉 d[k]에는 합이 k가 되기위한 동전의 경우 저장
d[0]=1 #합이 k가 되게 만들떄, k원 동전을 하나만 쓰는 경우 1
for c in coin:
    for i in range(c,k+1):
        d[i]+=d[i-c] #d[i]가 되기 위해서 i-c에서 c만큼 더하면 k가 되는 경우를 합함
print(d[k])

# 코드길이 : 436 B
# 시간 : 200 ms
# 메모리 : 31256 KB