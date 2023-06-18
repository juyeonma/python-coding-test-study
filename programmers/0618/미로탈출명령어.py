import sys

sys.setrecursionlimit(100000) #시간초과 남

direction = ['d', 'l', 'r', 'u']
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

answer = ""
ok=False
def solution(n, m, x, y, r, c, k):
    global answer
    def dfs(px,py,cnt,way):
        global answer, ok
        if ok: #최단경로를 발견했다면 종료
            return
        if abs(px-r)+abs(py-c)+cnt>k: #현재 남은 거리가 목표 거리보다 많이 남았으면 종료
            return
        if cnt>k: #목표 횟수를 초과하면 종료
            return
        if not ok and cnt==k: #최단경로를 아직 발견하지 않은 상태에서 목표 거리만큼 이동했다면
            if px==r and py==c: #도착지까지 왔는지 확인하고,
                ok=True # ok를 트루로
                answer=way #answer에 경로를 저장하고 return 하여 나중에 이 값이 출력됨
                return
        for i in range(4):
            nx = px+dx[i]
            ny = py+dy[i]
            if nx<1 or nx>n or ny<1 or ny>m:
                continue
            dfs(nx,ny, cnt+1, way+direction[i])
    z = k-abs(x-r)+abs(y-c) #목표 거리가 얼마나 남았는지
    if z<0 or z%2!=0: #z가 홀수이거나 0보다 작으면,,(이해 안됨)
        return "impossible"
    dfs(x,y,0,"")
    if not ok:
        return "impossible"
    return answer