#배열 두개를 통해서 코드를 짰는데 하나로 할 수 있을 것 같다
#내일 다시 해봐야겠다

# 처음에 문제를 잘못 이해하고 잘못봐서 문제만 한시간은 본 것 같다..
# 이 문제는 어렵다기보다는 복잡하고 흐름을 잘 파악하고 있는 것이 중요한 것 같다


n,m,k = map(int,input().split())
#파이어볼이 갈 수 있는 방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

board = [[0]*n for _ in range(n)]
d_state={True:[0,2,4,6],False:[1,3,5,7]} # 파이어볼이 나눠질때 방향 설정

fireball_info = [list(map(int,input().split())) for _ in range(m)] #파이어볼 정보 저장
#파이어볼 x,y 인덱스로 변경 (좀 비효율적인것같은데 어떻게 바꿀 수 있을까?)
for i in range(len(fireball_info)):
    fireball_info[i][0]-=1
    fireball_info[i][1]-=1

# k번 반복시키기
for i in range(1,k+1):
    storage = [[0]*n for _ in range(n)] #각 위치에서의 파이어볼 저장하기
    while len(fireball_info)!=0: # 파이어볼 모두 꺼내면서 확인
        r,c,m,s,d=fireball_info.pop()
        nx = (r+(dx[d]*s))%n
        ny = (c+(dy[d]*s))%n
        if board[nx][ny]!=i:
            board[nx][ny]=i
            storage[nx][ny]=[]
        storage[nx][ny].append([m,s,d]) # 파이어볼 위치 저장

    for j in range(n): # 보드를 돌면서
        for k in range(n):
            if board[j][k]==i: #해당 횟수에 해당할 때
                total_m=0
                total_s=0
                total_d=storage[j][k][0][2]
                cur_d_state=True
                if len(storage[j][k])>1: # 그 위치에 여러 개의 파이어볼이 있다면 분기처리
                    for m,s,d in storage[j][k]:
                        total_m+=m
                        total_s+=s
                        if total_d%2 == d%2: # 전체 방향이 짝수이거나 홀수라면
                            total_d=d
                        else: # 하나라도 다르면
                            cur_d_state=False
                    total_m//=5
                    total_s//=len(storage[j][k])

                    if total_m!=0:
                        for dir in d_state[cur_d_state]:
                            fireball_info.append([j,k,total_m,total_s,dir])
                else: # 파이어볼이 하나라면 그대로 다시 넣기
                    fireball_info.append([j,k,*storage[j][k][0]])

result=0
for x,y,m,s,d in fireball_info: # 파이어볼 정보 돌면서 질량더하기
    result+=m
                
print(result)   
    
