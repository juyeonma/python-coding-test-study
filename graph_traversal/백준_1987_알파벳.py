# 시간초과,, set으로 풀어야 하는 것 같다..
from collections import deque
r,c = map(int,input().split())
gragh=[]
# al=[]
for i in range(r):
    gragh.append(list(input()))

dx=[0,0,1,-1]
dy=[-1,1,0,0]

# visit=[[0]*c for _ in range(r)]
cnt=1

q=deque()
q.append((0,0,gragh[0][0]))
# visit[0][0]=1
# al.append(gragh[0][0])
while q:
    x,y,al = q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c and gragh[nx][ny] not in al:
            # al.append(gragh[nx][ny])
            # visit[nx][ny]=1
            q.append((nx,ny,al+gragh[nx][ny]))
            cnt=max(cnt,len(al)+1)
# print(al)
print(cnt)

#메모리 :  kb
#시간 :  ms
#코드길이 : 607 b
#풀이시간 : 약 1시간