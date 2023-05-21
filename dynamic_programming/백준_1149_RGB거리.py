n = int(input())
h = []
for _ in range(n):
    h.append(list(map(int, input().split())))


for i in range(1,n):
    h[i][0]=min(h[i-1][1],h[i-1][2])+h[i][0] #빨간집을 칠할때 최소값
    h[i][1]=min(h[i-1][0],h[i-1][2])+h[i][1] #초록집을 칠할때 최소값
    h[i][2]=min(h[i-1][0],h[i-1][1])+h[i][2] #파란집을 칠할떄 최소값

print(min(h[n-1]))

# 코드길이 : 368 B
# 시간 : 80 ms
# 메모리 : 31256 KB