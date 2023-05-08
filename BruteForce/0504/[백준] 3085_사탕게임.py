# 행의 위치 두개를 바꾸면 그 위치의 열 확인  (좌우)
# 열 위치 두개를 바꾸면 그위치의 행 확인     (상하)

# 자꾸 시간초과나서 답을봤는데 매커니즘이 같았다. 고민 끝에 함수로 빼서 확인해봤는데 통과되었다.
# 왜 함수로 빼서 코드를짜면 더 시간이 절약될까? 함수 사용이유는 가독성과 중복 코드를 없애기 위함이지 시간과는 관련없다고 생각했는데.. 
# 아시는 분 알려주세요..

# 인접한 곳만 검사하면 되고 모든 행과 열을 다 검사해야한다.
# 윗방향과 왼쪽방향으로 인접한 곳을 찾는 건 이미 그 전에 확인이 가능하기 때문에 오른쪽과 아래방향만 검사하면 된다.
# 딥카피로 풀까 했는데 시간복잡도가 마음에 걸려서 해당 위치를 변경하고 검사후에 다시 원래 상태로 돌려놓는 방식으로 하였다.
# 연속적인 사탕을 어떻게 고를까 고민하다가 각 갯수를 구할까를 생각도 해봤는데 굳이 그럴 필요 없고 이전인덱스의 값과 같은지를
# 확인하고 같으면 카운팅 다르면 최대값 갱신하고 다시 카운팅 하는 방식으로 하였다. 약간 투포인터 느낌으로 풀어보았다. 

N = int(input())
board = [list(input()) for _ in range(N)]

dx=[0,1]
dy=[1,0]
max_candy=0       # 먹을 수 있는 캔디의 최대값 구하기

def check(board):
    temp=0      # 캔디의 임시 최대값 >> 캔디의 위치를 바꾸고나서 저장해둘 캔디개수
    for i in range(N):      #각 행만큼 for문
        st=0        # 비교를 위한 첫번째인덱스
        en=0        # 비교를 위한 마지막 인덱스
        while en<N:       # 마지막인덱스가 범위를 넘어가게되면 while문 탈출
          if board[i][st]==board[i][en]:    # 두 값이 같으면 마지막인덱스 한칸이동
              en+=1
          else:
              temp=max(temp,en-st)    # 두 값이 달라지면 첫번째 인덱스를 마지막인덱스위치로 이동
              st=en
        temp=max(temp,en-st)    # 행for문이 끝나면 캔디 임시 최대값 갱신
    for i in range(N):      # 각 열만큼 for문
        st=0
        en=0
        while en<N:
          if board[st][i]==board[en][i]:
              en+=1
          else:
              temp=max(temp,en-st)
              st=en
        temp=max(temp,en-st)
    return temp       # 행,열 모두 돌고나서 최대값 반환

for i in range(N):
    for j in range(N):
        for dir in range(2): # 오른쪽과 아래쪽 방향으로 가는 경우
            nx=i+dx[dir]
            ny=j+dy[dir]
            if nx>=N or ny>=N:  #범위를 벗어나면 for문 한번 넘어가기
                continue
            board[i][j],board[nx][ny]=board[nx][ny],board[i][j]   # 인접한 위치 교환
            # temp=0
            # for k in range(N):
            #     st=0
            #     en=0
            #     while en<N:
            #       if board[k][st]==board[k][en]:
            #           en+=1
            #       else:
            #           temp=max(temp,en-st)
            #           st=en
            #     temp=max(temp,en-st)
            # for k in range(N):
            #     st=0
            #     en=0
            #     while en<N:
            #       if board[st][k]==board[en][k]:
            #           en+=1
            #       else:
            #           temp=max(temp,en-st)
            #           st=en
            #     temp=max(temp,en-st)
            # max_candy=max(max_candy,temp)
            max_candy=max(max_candy,check(board))   #check함수에서 구한 임시 캔디 최대값과 그 이전 최대값을 비교
            board[i][j],board[nx][ny]=board[nx][ny],board[i][j]   #캔디 위치 원위치

print(max_candy)
