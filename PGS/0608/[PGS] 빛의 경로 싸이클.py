# 못풀었다.. 솔직히 포기를 빨리 하긴 했다.
# 이 문제는 오래 생각하는 것보다 좋은 풀이를 보는 게 더 효율적이라고 판단햇서였다.

# 답을 보기 전에도 dfs로 풀어야겠다는 생각을 햇는데 각 경우에서 어떻게 방향을 정해줘야 할지 감이 안왔었다.
# 또한 시간복잡도를 제대로 확인하지 못해서 이걸 dfs로 풀어도 될 지 감이 안잡혔다.
# 역시 시간복잡도를 제대로 확인하는 게 중요하다
# 3차원 배열이 핵심

# 각 격자지점에서 모든 방향으로 나가는 빛의 경로를 탐색하는 문제
# 모든 격자지점을 탐색한다고 하더라도 방문한 곳이 있으면 이미 확인한 빛의 경로임을 알 수 있으므로 넘어가면 된다.

def solution(grid):
    answer = [] # 답을 담을 배열
    r,c=len(grid),len(grid[0])  # 격자 행렬의 길이
    board=[[[] for _ in range(c)] for _ in range(r)] # 각 격자 지점마다 빛의 방향을 담을 배열
    direction ={"L":[0,-1],"R":[0,1],"D":[1,0],"U":[-1,0]} # 빛의 방향 4가지 경로
    
    for x in range(r):  # 각 격자 지점을 돌리기 위한 for문
        for y in range(c):
            for d in 'ULDR':  # 빛의 방향설정
                cnt=0 # 격자지점을 이동할때마다 카운팅
                while d not in board[x][y]: # 방문한 빛의 방향이 아니라면 계속 빛은 진행한다
                    board[x][y].append(d) # 해당 격자의 사용한 방향은 방문처리
                    cnt+=1  #격자를 지나쳤기 때문에 카운팅
                    
                    x = (x+direction[d][0]) % r # 범위를 넘어가면 반대쪽 끝으로 돌아가야하기때문에 모듈러 처리
                    y = (y+direction[d][1]) % c
                    # "S"의 경우 방향 이동할 필요가 없기 때문에 기존의 d를 그대로 사용
                    if grid[x][y] =="L":  # "L"과 "R"은 방향 이동이 필요하기 때문에 조건 걸어주기
                        idx = "ULDR".index(d)
                        d = "ULDR"[(idx+1)%4]
                    elif grid[x][y] =="R":
                        idx = "RDLU".index(d)
                        d="RDLU"[(idx+1)%4]
                if cnt: # 카운팅이 되었다는 것은 다른 빛의 이동경로가 존재햇다는 뜻이므로 배열에 담기
                    answer.append(cnt)
    return sorted(answer) # 정답은 오름차순으로 소팅한 배열 반환
# 참고 https://codinghejow.tistory.com/193


# def solution(grid):
#     answer = []
#     r,c=len(grid),len(grid[0])
#     board=[[[] for _ in range(c)] for _ in range(r)]
#     direction = [(-1,0),(0,1),(1,0),(0,-1)] # 상우하좌
#     for x in range(r):
#         for y in range(c):
#             for d in range(4):
#                 cnt=0
#                 while d not in board[x][y]:
#                     board[x][y].append(d)
#                     cnt+=1
                    
#                     x = (x+direction[d][0]) % r
#                     y = (y+direction[d][1]) % c
                    
#                     if grid[x][y] =="L":
#                         d = (d-1)%4
#                     elif grid[x][y] =="R":
#                         d = (d+1)%4
#                 if cnt:
#                     answer.append(cnt)
#     return sorted(answer)


#다시 풀어본 것
# def solution(grid):
#     answer = []
#     r,c= len(grid),len(grid[0])
#     board=[[[0,0,0,0] for _ in range(c)] for _ in range(r)]
#     dx=[1,0,-1,0]#하우상좌
#     dy=[0,1,0,-1]
#     for x in range(r):
#         for y in range(c):
#             for dir in range(4):
#                 cnt=0
#                 while not board[x][y][dir]:
#                     board[x][y][dir]=1
#                     cnt+=1
#                     x=(x+dx[dir])%r
#                     y=(y+dy[dir])%c
                    
#                     if grid[x][y]=="L":
#                         dir=(dir-1)%4
#                     elif grid[x][y]=="R":
#                         dir=(dir+1)%4
#                 if cnt:
#                     answer.append(cnt)
                    
#     return sorted(answer)