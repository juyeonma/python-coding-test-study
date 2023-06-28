# 예시는 맞는데 백준에 돌리면 틀리다고 나옴, 다시 풀기
r,c = map(int, input().split())
gragh=[[0]*c for _ in range(r)]
copy=[[0]*c for _ in range(r)]
for i in range(r):
    x=input()
    for j in range(len(x)):
        if x[j]=="X":
            gragh[i][j]=1
            copy[i][j]=1
    
dx=[0,0,1,-1]
dy=[-1,1,0,0]

for i in range(r):
    for j in range(c):
        if gragh[i][j]==1:
            cnt=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0>nx or r<=nx or 0>ny or c<=ny:
                    cnt+=1
                else:
                    if gragh[nx][ny]==0:
                        cnt+=1
            if cnt>2:
                copy[i][j]=0
                
row,col=[],[]
dic={0:".",1:"X"}

for i in range(r):
    for j in range(c):
        if copy[i][j]==1:
            row.append(i)
            col.append(j)
if row:
    row_l = min(row)
    row_h=max(row)
    col_l = min(col)
    col_h = max(col)
    for i in range(row_l,row_h+1):
        for j in range(col_l,col_h+1):
            print(dic[copy[i][j]],end=" ")
        print()
else:
    print("X")

# 메모리 : 31256 KB
# 시간 : 40 ms
# 코드길이 : 889 B