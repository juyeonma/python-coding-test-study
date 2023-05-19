n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

d=[0]*(n)

if len(stair)<=2:
    print(sum(stair))

else:
    #두번째 계단까지는 각 숫자들을 합한 값을 저장
    d[0]=stair[0]
    d[1]=stair[0]+stair[1]
    for i in range(2,n):
        d[i]=max(d[i-3]+stair[i-1]+stair[i], d[i-2]+stair[i]) 
        #2계단을 연속으로 걸었을 때, 1계단을 건너뛰고 걸었을때 큰값 비교
        #i계단에 도착할 때, 전 계단을 밟고 올라온건지, 전 계단을 건너뛰고 올라왔는지 비교
    print(d[-1])
    
# 코드길이 : 454 B
# 시간 : 52 ms
# 메모리 : 31256 KB