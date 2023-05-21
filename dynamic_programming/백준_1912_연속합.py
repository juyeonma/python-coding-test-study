n = int(input())
x = list(map(int, input().split()))

d=[0]*n

if n<=1:
    print(sum(x))
else:
    d[0]=x[0] #가장 첫번째는 자기 자신으로 초기화
    for i in range(1,n):
        d[i]=max(x[i],d[i-1]+x[i]) #자기 자신 1개와 그 전단계와의 합들을 비교해서 큰값 저장
    print(max(d)) #그 값들 중에 제일 큰 값 출력
    
# 코드길이 : 187 B
# 시간 : 92 ms
# 메모리 : 38964 KB