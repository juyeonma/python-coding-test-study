# 처음 문제를 보고 벙쪘다.. 울타리 선정기준이 여러가지가 될 수 있는 것 아닌가 싶었기 때문이다
# 근데 진짜였다..
# 주력언어가 js인데 js는 join을 사용할 때 pasture[i].join("") 이런식으로 사용한다. 그래서 join사용할 때나 여러 모듈을 사용할 때 자주 헤갈리는것같다.

# 모든 곳에 전부 울타리 설치하기
# 양의 주변에 늑대있으면 0출력 후 탈출
# 양의 주변에 늑대없으면 1출력후 울타리 출력

#첫번째 풀이
# bfs로구만 queue를써야겠어 라고 생각하고 푼 풀이이다
# 그런데 굳이 그럴 필요없고 처음 목장을 돌면서 양 주변의 위치만 확인하면 되므로 두번째 풀이처럼 풀면 더 효율적으로 풀 수 있다.
from collections import deque
import sys

R,C = map(int,input().split())

pasture = [list(input()) for _ in range(R)]

queue =deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(R):
    for j in range(C):
        if pasture[i][j]==".":
            pasture[i][j]="D"
        if pasture[i][j]=="S":
              queue.append((i,j))

while queue:
    x,y=queue.popleft()
    for dir in range(4):
        nx=x+dx[dir]
        ny=y+dy[dir]
        if nx<0 or ny<0 or nx>=R or ny>=C:
            continue
        if pasture[nx][ny]=="W":
            print(0)
            sys.exit()
else:
    print(1)
    for i in range(R):
        print("".join(pasture[i]))
#메모리 39192KB 시간 292ms

# 두번째 풀이

# import sys

# R,C = map(int,input().split())
# pasture = [list(input()) for _ in range(R)]

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# for i in range(R):
#     for j in range(C):
#         if pasture[i][j]=="S":
#             for dir in range(4):
#                 nx=i+dx[dir]
#                 ny=j+dy[dir]
#                 if nx<0 or ny<0 or nx>=R or ny>=C:
#                     continue
#                 if pasture[nx][ny]=="W":
#                     print(0)
#                     sys.exit()
#                 if pasture[nx][ny]==".":
#                     pasture[nx][ny]="D"
# else:
#     print(1)
#     for i in range(R):
#         print("".join(pasture[i]))

#메모리 32440KB 시간 232ms