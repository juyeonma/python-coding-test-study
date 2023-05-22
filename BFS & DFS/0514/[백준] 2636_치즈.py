#(0,0)부터 주변에 1을 찾는다
# 주변에 1이 있으면 카운팅, 1은 queue에 넣지말기,square 배열에서 0으로 초기화, vis는 1로 초기화
# vis 1은 넘어가기 
#  반복
# 다 돌았는데 모두 0이라면 횟수랑 개수 출력

# 한번에 맞았다... 몇 번 틀리는 게 익숙한데 한번에 맞아서 느낌이 이상했다..
# 코드를 어떻게 짤지 생각하고 적어두고 푸는게 진짜 좋은 것 같다.

# 아이디어가 처음부터 바로 생각나지는 않아서 고민하다가 풀었다.
# 아직 논리력이 부족한 것 같다. 풀고나서도 살짝 의심이 들곤 한다.

from collections import deque

h,w = map(int,input().split())
square = [list(map(int,input().split())) for _ in range(h)]
count=0 # 치즈가녹는데 걸리는 시간
cheeze_num=0  # 치즈가 와전히 녹기 한 시간 전의 치즈칸수

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs():
    global cheeze_num
    queue= deque([(0,0)]) # 첫번째 위치부터 돌면서 1을 찾기 위해 (0,0)을 넣었다.
    vis = [[0]*w for _ in range(h)] # 방문한 위치 배열
    vis[0][0]=1
    cnt=0
    while queue:
        x,y=queue.popleft()
        for dir in range(4):
            nx= x + dx[dir]
            ny= y + dy[dir]
            if nx<0 or ny<0 or nx>=h or ny>=w:  # 범위 벗어나면 넘어가기
                continue
            if vis[nx][ny]: # 이미 방문한곳은 넘어가기
                continue
            vis[nx][ny]=1
            if square[nx][ny]:  # 치즈 위치라면
                cnt+=1  # 카운팅하기
                square[nx][ny]=0  # 치즈 녹이기
                continue
            queue.append((nx,ny))
    if cnt>0: #cnt가 0을 넘었다는 건 치즈가 있다는 뜻 
        cheeze_num=cnt  # 치즈개수를 갱신
        return True
    else: # 치즈개수가 0이라면 따로 갱신하지않고 이전 치즈개수 그대로 변수에 남긴 상태
        return False
                
while True:
    if not bfs(): # 치즈가 다 녹은 상태라면
      break  # 멈추기
    count+=1  # 한시간마다 1증가시키기

print(count)
print(cheeze_num)


