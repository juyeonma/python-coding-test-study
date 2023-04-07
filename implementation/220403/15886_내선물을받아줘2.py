n = int(input())
m = list(input())
cnt=0

for i in range(n-1):
    if m[i:i+2]=='EW':
        #어느 곳에 시작하든 WE가 있는 곳에 머무르게 됨
        cnt+=1
print(cnt)