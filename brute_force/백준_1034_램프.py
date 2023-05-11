n, m = tuple(map(int, input().split()))
lamp = []
for _ in range(n):
    lamp.append(input())
k = int(input())

cnt = 0

for j in range(n):
    zero = 0
    for num in lamp[j]:
        if num=='0':
            zero+=1 #행별로 0의 개수 구하기
    light=0 #현재 행과 같은 값을 가진 행 개수 세기
    if zero<=k and zero%2==k%2: #0의 개수가 스위치를 누르는 횟수보다 작거나 같아야됨, 또는 나머지의 수가 같아야함
        for i in range(n):
            if lamp[i]==lamp[j]:
                light+=1
    cnt = max(cnt, light) #가장 많은 수를 저장
print(cnt)

#코드길이 : 532B
#시간 : 44ms