a = list(input())
b = list(input())

al = len(a)
bl = len(b)

d=[[0]*(bl+1) for _ in range(al+1)]
#이차원배열로 비교
for i in range(1,al+1):
    for j in range(1,bl+1):
        if a[i-1]==b[j-1]: #같은 알파뱃 배열을 가진 경우
            d[i][j]=d[i-1][j-1]+1 #그 전에 값에 1을 더함
        else: 
            d[i][j]=max(d[i-1][j],d[i][j-1]) #그렇지 않으면 최대값을 저장
print(d[-1][-1])

# 코드길이 : 288 B
# 시간 : 508 ms
# 메모리 : 55712 KB