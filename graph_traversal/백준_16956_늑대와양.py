n,m=map(int, input().split())

gragh=[]

for i in range(n):
    gragh.append(list(input()))
    
dx=[0,1,0,-1] #동남서북
dy=[1,0,-1,0]
safe=True
for i in range(n):
    for j in range(m):
        if gragh[i][j]=='W':
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                elif gragh[nx][ny]=='S':
                    safe=False
        elif gragh[i][j]=='S':
            continue
        else:
            gragh[i][j]='D'

if safe==True:
    print(1)
    for i in range(n):
        for j in range(m):
            print(gragh[i][j], end='')
        print()
else:
    print(0)