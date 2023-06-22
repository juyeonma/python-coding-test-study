from collections import deque

def bfs(p):
    start=[]
    for i in range(5):
        for j in range(5):
            if p[i][j]=="P":
                start.append([i,j]) #사람이 앉은 자리 정보만 저장
    for s in start: #사람 정보를 기준으로 탐색
        q=deque([s])
        visit=[[0]*5 for _ in range(5)]
        dist = [[0]*5 for _ in range(5)]
        visit[s[0]][s[1]]=1 #사람이 앉은 자리는 1
        
        while q:
            y,x=q.popleft()
            dx=[-1,1,0,0]
            dy=[0,0,-1,1]
            
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if 0<=nx<5 and 0<=ny<5 and visit[ny][nx]==0: #주변 탐색
                    if p[ny][nx]=="O": #빈자리가 나온다면
                        q.append([ny,nx]) #해당 위치 저장
                        visit[ny][nx]=1 #방문표시
                        dist[ny][nx]=dist[y][x]+1 #거리를 더함(맨해튼거리)
                    if p[ny][nx]=="P" and dist[y][x]<=1: #다음 탐색위치가 P이면서 거리가 1보다 작으면 거리두기를 지키지 못한것
                        return 0 #0을 리턴
    return 1 

def solution(places):
    answer = []
    
    for i in places: #대기실 마다 탐색해야되니까
        answer.append(bfs(i))
    
    return answer
