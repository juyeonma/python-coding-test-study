# 참고 : https://velog.io/@soobin519/Python-%EB%B0%B1%EC%A4%80-2631-%EC%A4%84%EC%84%B8%EC%9A%B0%EA%B8%B0
import sys
input = sys.stdin.readline

n = int(input())

d = [1]*(n+1)
num = [0]
for i in range(n):
    num.append(int(input()))

#가장 긴 증가하는 수열 찾기 
for i in range(1,n+1):
    for j in range(1,i):
        if num[j]<num[i]:
            d[i]=max(d[i],d[j]+1)

#n- 긴 증가하는 부분수열의 길이 
print(n-max(d))

# 가장 긴 증가하는 수열 찾기 => 엄청 많이 했는데 자꾸 까먹고 어디에서 응용해야할지를 못 생각하는 것 같다..
# => 공부 더 하기..!