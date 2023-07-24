# 못 풀었다.
# 시간초과에 계속 당하다보니까 7명의 학생을 뽑아서 그 7명이 붙어있는 것을 확인하는 걸 해볼 생각을 못했다
from collections import deque

students = [list(input()) for _ in range(5)]
result=0
selected_students = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(arr):
    vis = [[1]*5 for _ in range(5)]
    for x,y in arr:
        vis[x][y]=0

    q = deque([(arr[0])])
    vis[arr[0][0]][arr[0][1]]=1
    cnt=1
    while q:
        x,y=q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or ny<0 or nx>=5 or ny>=5:
                continue
            if vis[nx][ny]:
                continue
            cnt+=1
            vis[nx][ny]=1
            q.append((nx,ny))
    
    if cnt==len(arr):
        return True
    else:
        return False

def select_students(depth,st,y_cnt):
    global result

    if y_cnt>3:
        return
    
    if depth == 7:
        if bfs(selected_students):
            result+=1
        return

    for i in range(st,25):
        r = i // 5
        c = i % 5
        selected_students.append((r,c))
        select_students(depth+1, i+1, y_cnt+(students[r][c]=="Y"))
        selected_students.pop()

select_students(0,0,0)
print(result)