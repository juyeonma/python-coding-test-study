# 맨 처음 시도는 dx,dy에 모든 가능한 거리를 넣고 풀려했는데 생각해보니 논리에 오류가 있어 방향을 틀었다
# 2번째 시도에서는 p를 한번에 큐에넣고 판단하려고 했는데 잘 안됐다
# 행렬의 길이가 5로 고정되어있길래 시간초과의 문제는 없을 것으로 판단하고 각 p마다 bfs를 돌렸다
# 그런데 이 풀이는 n이 커지면 적용하기 힘든 풀이인 것 같다
# 익숙한 bfs 문제 같은데 생각보다 오래 걸렸다.. 공부가 더 필요한 것 같다

# 익숙한 문제라고 생각하고 별 생각없이 코드를 짜니까 이렇게 시행착오를 겪는다
# 익숙하더라도 어떻게 짤지 다 생각하고 풀자
 
# 모든 p를 큐에 넣고 한번에 돌리는 방법이 있을까?
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(case):
    for i in range(5):
        for j in range(5):
            if case[i][j]=="P": # 각 p마다 bfs 돌리기
                q=deque()
                q.append((i,j))
                vis=[[-1]*5 for _ in range(5)]
                vis[i][j]=0
                while q:
                    x,y=q.popleft()
                    for dir in range(4):
                        nx= x+dx[dir]
                        ny= y+dy[dir]
                        if nx<0 or ny<0 or nx>=5 or ny>=5:
                            continue
                        if vis[nx][ny]==0:
                            continue
                        if case[nx][ny]=="P": # 도달한 위치가 p라면 2이에 맞닿으므로 False
                            return 0
                        if case[nx][ny]=="X": # 벽이면 통과
                            continue
                        vis[nx][ny]=vis[x][y]+1 # O라면 전위치에서 1더해줌
                        if vis[nx][ny]==2: # 그게 2라면 큐에 넣지 말고 통과
                            continue
                        q.append((nx,ny))
    return 1

def solution(places):
    answer = []
    for place in places: # 각 경우별로 확인하기 
        answer.append(bfs(place))
    return answer

#40분


# 이런 풀이도 있었다.
# bfs가 아닌 좌표 차이를 통해 2중 for문을 사용한 방식이다
# 모든 P의 좌표를 담은 후 좌표별로 모두 비교한다

def check(place):
    arr= []
    for i in range(5): # P 좌표 담기
        for j in  range(5):
            if place[i][j]=="P":
                arr.append((i,j))
    
    for x1,y1 in arr: #각좌표 모두 비교
        for x2,y2 in arr:
            if x1==x2 and y1==y2: # 같은 값이라면 같은 위치이기 때문에 통과
                continue
            if abs(x1-x2)+abs(y1-y2)==1: # 차이가 1이라면 거리두기 실패
                return 0
            if abs(x1-x2)+abs(y1-y2)==2: # 차이가 2일때
                if x1-x2==0 or y1-y2==0: # 수직선상이나 수평선상에 위치할 때 파티션이 없다면 실패
                    if place[(x1+x2)//2][(y1+y2)//2]!="X":
                        return 0
                else: # 대각선에 위치하지만 파티션 두개가 모두 존재하지 않으면 실패
                    if place[x1][y2]!="X" or place[x2][y1]!="X":
                        return 0
    return 1 # 하나라도 실패하지 않고 모두 검사를 햇다는건 모두 거리두기 성공

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer