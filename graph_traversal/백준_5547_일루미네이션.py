'''
# 백준_5547_일루미네이션. 골드 4. 풀이: 23.07.09

# How to
- 육각형
- 빈 공간: 0, 방문 전 건물: 1, 방문한 빈 공간: 2

## 1.
- 맵의 테두리만 탐색한다.
    - 빈 공간일 경우: BFS로 맞닿은 건물의 경계를 정답에 추가
    - 건물일 경우: 맵 바깥과 맞닿은 경계를 정답에 추가
- 이때 행의 홀수번 or 짝수번에 따라 연결된 부위 탐색이 달라진다.
- 한번 방문한 빈 공간은 2로 표시하여 재방문 방지

## 2. 가짜 테두리 추가
- 1번 방법에서 테두리만 탐색한것이 번거로워서, 애초에 가짜 테두리를 추가.
    - 상하좌우에 각각 1칸씩 빈 공간이 추가됨.
- bfs(0, 0) 만 해도 모든 빈 공간이 연결되기 때문에 별도로 건물의 맵 경계선 탐색을 안해도 됨.
- 가짜 테두리가 1칸씩 생겼으므로, 인덱스 1부터 시작.
    - 1번에서 짝수 행은 이번에 홀수 행으로, 홀수 행은 이번에 짝수 행으로 바뀜
    - dx는 통일하고, dy를 y의 홀짝에 따라 list에 넣음
    

## 반례
건물에 둘러쌓인 닫힌 구멍이 여러개인 경우
4 3
1 1 1 1
1 0 0 1
1 1 1 1
답: 26


# Review
- 건물에 둘러쌓인 빈 공간은 경계를 세지 않는데, 이 구멍이 여러개 붙어있는 반례에서 고생했다.
- 처음에는 건물에서 bfs 탐색을 시작하여 빈 공간과의 경계값을 셌지만,
빈 공간에서 bfs 탐색을 시작하여 건물과의 경계를 세는게 더 낫다는걸 깨달았다.
- 이렇게 시간이 많이 걸리고 이렇게 긴 코드가 나올지 몰랐다. 
- 처음엔 육각형에 당황했지만, 결국 일반적인 배열과 같다는걸 다 풀고 나서야 깨달았다.
'''


# 1. 성공
from collections import deque
import sys
input = sys.stdin.readline

# w: 열, h: 행
w, h = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(h)]

# y: 행, x: 열
# 짝수 행
dy1 = [0, -1, 1, -1, 0, 1]
dx1 = [-1, 0, 0, 1, 1, 1]

# 홀수 행
dy2 = [-1, 0, 1, -1, 1, 0]
dx2 = [-1, -1, -1, 0, 0, 1]

cnt = 0

# 행의 홀수번 or 짝수번에 따라 연결된 부위 탐색이 달라진다.
def dxdy(y):
    # 홀수 행
    if y % 2:
        return dy2, dx2
    # 짝수 행
    return dy1, dx1


# 빈 공간일 경우, 건물과의 경계를 cnt에 추가
def bfs(y, x):
    global cnt
    # 큐에 넣고 방문표시
    q = deque([(y, x)])
    house[y][x] = 2
    while q:
        y, x = q.popleft()
        # 행이 홀수번인지 짝수번인지에 따라 dx, dy 결정
        dy, dx = dxdy(y)

        for j, i in zip(dy, dx):
            ny = y + j
            nx = x + i
            
            # 범위 안일 경우
            if 0 <= ny < h and 0 <= nx < w:
                # 건물일 경우,
                if house[ny][nx] == 1:
                    cnt += 1
                
                # 아직 방문하지 않은 빈 공간일 경우, 큐에 넣고 방문표시
                elif house[ny][nx] == 0:
                    q.append((ny, nx))
                    house[ny][nx] = 2
                    
                # 이미 방문한 빈 공간(house[ny][nx] == 2)인 경우, 넘어감
                
                
# 건물일 경우, 맵 바깥과의 경계를 cnt에 추가
def outside(y, x):
    global cnt
    # 행이 홀수번인지 짝수번인지에 따라 dx, dy 결정
    dy, dx = dxdy(y)
    for j, i in zip(dy, dx):
        ny = y + j
        nx = x + i
        # 맵을 벗어났다면, 즉 맵의 경계라면: cnt에 추가
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            cnt += 1
            
            
# 맵의 테두리만 탐색하기 위하여: x, y 범위를 넣고 cnt 구하기      
def solve(y_range, x_range):
    for y in y_range:
        for x in x_range:
            # 빈 공간일 경우, 건물과의 경계를 cnt에 추가
            if house[y][x] == 0:
                bfs(y, x)

            # 건물일 경우, 맵 바깥과의 경계를 cnt에 추가
            elif house[y][x] == 1:
                outside(y, x)  


# 맵의 상단과 하단 테두리만 탐색
solve([0, h-1], range(w))
# 맵의 왼쪽과 오른쪽 테두리만(상단, 하단과 중복은 뺌) 탐색
solve(range(1, h-1), [0, w-1])            
 
print(cnt)


# 2. 성공: 가짜 테두리 만들기
# 34176 KB, 80 ms
from collections import deque
import sys
input = sys.stdin.readline

# w: 열, h: 행
w, h = map(int, input().split())

nw, nh = w+2, h+2
# 상하좌우에 1칸씩 더 있는 빈 맵을 만들고, 맵을 채워 넣음
house = [[0]*(nw) for _ in range(nh)]
for i in range(1, h+1):
    house[i][1:w+1] = map(int, input().split())

# 6개의 새로운 좌표 탐색
dy = [-1, -1, 0, 0, 1, 1]
# 가짜 테두리가 1칸씩 생겼으므로, 인덱스 1부터 시작
# y: 짝수 행(y % 2 = 0), 홀수행(y % 2 = 1)
dx = [[-1, 0, -1, 1, -1, 0], [0, 1, -1, 1, 0, 1]]

cnt = 0

# y: 행, x: 열
# 빈 공간일 경우, 건물과의 경계를 cnt에 추가
def bfs(y, x):
    global cnt
    # 큐에 넣고 방문표시
    q = deque([(y, x)])
    house[y][x] = 2
    while q:
        y, x = q.popleft()
        # 행이 홀수번인지 짝수번인지에 따라 dy 결정
        for j, i in zip(dy, dx[y % 2]):
            ny = y + j
            nx = x + i
            
            # 범위 안일 경우
            if 0 <= ny < nh and 0 <= nx < nw:
                # 건물일 경우,
                if house[ny][nx] == 1:
                    cnt += 1
                
                # 아직 방문하지 않은 빈 공간일 경우, 큐에 넣고 방문표시
                elif house[ny][nx] == 0:
                    q.append((ny, nx))
                    house[ny][nx] = 2
                    
                # 이미 방문한 빈 공간(house[ny][nx] == 2)인 경우, 넘어감
    
    # 정답 개수 출력
    return cnt

# 맵 바깥에 1칸씩 새로운 테두리가 존재하므로, 모든 빈 공간은 이어져있음.
print(bfs(0, 0))


'''
# Result
풀이 시간: 2시간
메모리: 34240 KB
시간: 76 ms
코드 길이: 2526 B
'''