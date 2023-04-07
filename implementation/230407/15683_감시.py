import copy
n,m = map(int, input().split())
cctv = []
gragh=[]

for i in range(n):
    gragh.append(list(map(int, input().split())))

for i in range(n):   
    for j in range(m):
        if gragh[i][j] in [1,2,3,4,5]:
            cctv.append((gragh[i][j],i,j))

mode=[[],
      [[0],[1],[2],[3]],
      [[0,2],[1,3]],
      [[0,1],[1,2],[2,3],[0,3]],
      [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
      [[0,1,2,3]]
      ]

dx=[-1,0,1,0] #북동남서
dy=[0,1,0,-1]

def fill(gragh,mode,x,y):
    for i in mode:
        nx=x #0부터 시작하는게 아니고 cctv정보에 따라 시작하니까
        ny=y
        while True:
            nx+=dx[i]
            ny+=dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                break
            if gragh[nx][ny]==6:
                break
            elif gragh[nx][ny]==0: #감시 가능한 곳이면 -1이라 저장
                gragh[nx][ny]=-1
                
def dfs(depth,gragh):
    global min_val
    if depth==len(cctv):
        cnt=0
        for i in range(n):
            cnt+=gragh[i].count(0)
        min_val=min(min_val,cnt)
        return
    temp= copy.deepcopy(gragh) #감시 방향 경우의 수에 따른 새로운 그래프 복사
    cctv_num,x,y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp,i,x,y)
        dfs(depth+1,temp)
        temp = copy.deepcopy(gragh)
        
min_val=int(1e9)
dfs(0,gragh)
print(min_val)