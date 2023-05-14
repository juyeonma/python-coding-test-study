import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 이거 안넣어주면 런타임 에러남

def dfs(x,y):
    dx=[0, 0, 1, -1, -1, 1, 1, -1] # 동서남북 대각선(4)
    dy=[-1, 1, 0, 0, -1, -1, 1, 1]
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        visit[x][y]==1
        if nx>=0 and nx<h and ny>=0 and ny<w:
            if gragh[nx][ny]==1 and visit[nx][ny]==0:
                visit[nx][ny]=1
                dfs(nx,ny)
    
while True:
    w,h = map(int,input().split())
    cnt=0
    if w==0 and h==0:
        break
    gragh=[]
    for _ in range(h):
        gragh.append(list(map(int, input().split())))
        
    visit=[[0]*w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if gragh[i][j]==1 and visit[i][j]==0: #visit 함수 조건도 고려해야됨(안하면 다 세어진다)
                dfs(i,j)
                cnt+=1
    print(cnt)
    
# 코드 길이 : 895 B
# 시간 : 68 ms
# 메모리 : 32644 KB