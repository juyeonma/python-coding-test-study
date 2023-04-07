n = int(input())
gragh=[[0]*101 for _ in range(101)]

dx=[0,-1,0,1] #동북서남
dy=[1,0,-1,0]

for i in range(n):
    y,x,d,g = map(int,input().split())
    gragh[x][y]=1 #시작위치
    
    curve=[d] #시작방향을 넣어서 방향을 더해감
    for j in range(g):
        for k in range(len(curve)-1,-1,-1):
            curve.append((curve[k]+1)%4) #90도 돌린거를 추가
            
    for j in range(len(curve)): #완성된 커브리스트 안에서 반복
        x+=dx[curve[j]] #해당 위치에서 커브 리스트만큼 이동
        y+=dy[curve[j]]
        if x<0 or x>=101 or y<0 or y>=101: 
            continue
        
        gragh[x][y]=1 #이동한 값에 1 저장
        
ans=0
for i in range(100):
    for j in range(100):
        #정사각형으로 커브가 만들어지면
        if gragh[i][j]==1 and gragh[i+1][j]==1 and gragh[i][j+1]==1 and gragh[i+1][j+1]==1:
            ans+=1 #개수 추가
            
print(ans)