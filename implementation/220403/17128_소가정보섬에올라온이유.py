n,q = map(int, input().split())
a = list(map(int, input().split()))
qq = list(map(int, input().split()))
sum_s=[0]*n
for i in range(n):
    sum_s[i]=a[i]*a[i-1]*a[i-2]*a[i-3] #미리 곱을 계산하여 담음

result=sum(sum_s) #담은 곱들의 합을 계산
for i in qq: #장난친거
    for j in range(4): #장난친 값이 4번 포함되니까
        new=(i-1+j)%n #
        sum_s[new]=-sum_s[new] #-를 붙였으므로 값이 -가 됨
        result+=2*sum_s[new] #원래 있던 값을 빼고, -붙인만큼 또 빼야되니까
    print(result)