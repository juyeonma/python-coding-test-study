# 2차원 배열로 표를 만들고 채워나가면서 확인하면 규칙을 찾을 수 있다.
#   0 1 2 3 4 5 6 7 8 9
# 1 0 1 1 1 1 1 1 1 1 1
# 2 1 2 2 2 2 2 2 2 2 1
# 3 2 3 4 4 4 4 4 4 3 2
# ...

n = int(input())
d = [[0]*10 for _ in range(n+1)]
d[1]=[0]+[1]*9

for i in range(2,n+1):
    for j in range(10):
        if j==0:
            d[i][j] = d[i-1][1]
        elif j==9:
            d[i][j] = d[i-1][8]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
    
print(sum(d[n])%1000000000)