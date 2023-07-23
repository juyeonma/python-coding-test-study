'''
# 백준_9663_N-Queen. 골드 4. 풀이: 23.07.16 -> 실패 -> 성공(풀이 2)

# How to
- 체스 퀸 규칙:
    - 일직선으로 앞, 뒤, 옆, 대각선 어떤 방향이든 원하는 만큼 이동할 수 있다.
    - 단 자기 기물은 뚫고 지나갈 수 없다.
    - 상대방 기물을 잡으면 수가 종료.
    
- 퀸이 한번에 갈 수 없는 위치, 8개 중 이후꺼 4개
dx = [1, 1, 2, 2]
dy = [-2, 2, -1, 2]

. X . X .
X . . . X 
. . Q . .
X . . . X
. X . X .


## 2. 행, 열, 대각선을 1차원 배열로: 성공
- 스터디원이 공유해준 바킹독의 알고리즘으로 풀이: https://blog.encrypted.gg/945
- 퀸은 같은 행, 열, 대각선에 1개씩만 놓을 수 있음을 이용
- 2차원 배열을 1차원으로 피고, O(1)로 접근함으로써 시간안에 해결 가능.


# Review
- 풀이 시간:
- 체스 규칙을 몰라서, 찾아봤다.
- 실패: 답이 계속 0이 나온다. 즉 퀸을 n개까지 못 놓는다.
    - 다음 좌표를 어떻게 탐색해야할까?

- 스터디원의 풀이가 신박했는데, 공유해준 바킹독의 알고리즘 설명을 보니 성공.
    - 2차원 배열을 1차원으로 피고, 인덱스로 접근해서 시간을 확 줄이는게 포인트였다.
- 진짜.. 내가 얼마나 익숙한 방법으로, 굳어진 방법으로만 풀려고 했는지 반성이 된다.
- 이렇게 생각하는 힘을 길러야겠다..!
- 그리고 늘 시간초과를 피하기 위해서, 시간을 줄이는 방법을 고민하고 고려해서 풀어야겠다.
'''

# Code
# 1. 실패
## 메모리:  KB, 시간:  ms
n = int(input())

dx = [1, 1, 2, 2]
dy = [-2, 2, -1, 2]

answer = 0

def check(x, y):
    # 해당 좌표가 범위 안인지,
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    # 이미 방문한건 아닌지
    if chess[x][y]:
        return False
    
    # 행
    for ii in range(n):
        if chess[x][ii]:
            return False

    # 열
    for ii in range(n):
        if chess[ii][y]:
            return False
        
    # 대각선
    for ix, iy in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
        for ii in range(1, n):
            nx, ny = x+ii*ix, y+ii*iy
            if 0 <= nx < n and 0 <= ny < n and chess[nx][ny]:
                return False
            
    return True
            
def dfs(x, y, cnt):
    global answer
    
    # 퀸을 n개 다 높은 경우, 경우의 수 +1
    if cnt == n:
        answer += 1
        return
    
    for i, j in zip(dx, dy):
        nx, ny = x + i, y + j
        # 높아도 된다면,
        if check(nx, ny):
            chess[nx][ny] = True
            dfs(nx, ny, cnt+1)
            chess[nx][ny] = False

# 모든 좌표 탐색
for x in range(n):
    for y in range(n):
        chess = [[False] * n for _ in range(n)]
        dfs(x, y, 0)
    
print(answer)


# 2. 행, 열, 대각선을 1차원 배열로: 성공
## 바킹독 설명 참고
## 메모리: 31256 KB, 시간: 23208 ms

n = int(input())

# 열, 오른쪽 대각선 ↘, 왼쪽 대각선 ↙
visited_col = [False] * n
visited_cross_right = [False] * (2*n-1)
visited_cross_left = [False] * (2*n-1)

answer = 0
def backtracking(x):
    global answer
    # 행마다 1개씩만 놓을 수 있으므로, n개 행에 다 퀸을 놓았다면, 정답 +1
    if x == n:
        answer += 1
        return
    
    for y in range(n):
        # 같은 열, 같은 오른쪽 대각선, 같은 왼쪽 대각선에 퀸이 있다면: 놓을 수 없음.
        if visited_col[y] or visited_cross_right[x+y] or visited_cross_left[x+n-1-y]:
            continue
        
        # 방문 체크하고,
        visited_col[y] = True
        visited_cross_right[x+y] = True
        visited_cross_left[x+n-1-y] = True
        
        # 재귀 들어가고(그 다음 행에 퀸을 놓는것),
        backtracking(x+1)
        
        # 다시 방문 체크 해제.
        visited_col[y] = False
        visited_cross_right[x+y] = False
        visited_cross_left[x+n-1-y] = False
 
# 0행에 퀸을 놓는 것부터 시작
backtracking(0)

print(answer)