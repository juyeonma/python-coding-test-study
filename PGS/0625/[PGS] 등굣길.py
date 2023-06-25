# 전에 풀었던 문제와 비슷한 문제였다. 우유도시였나?
# 물웅덩이 위치를 거르는 부분에서 i,j가 바뀌어 있는지 모르고 계속 틀렸었다. 겸손하게 문제 똑바로읽자
# bfs로 풀 수도 있지만, 지났던 위치를 계속 지나야 된다는 점에서 시간이 오래걸린다
# 그래서 해당 위치까지 올수 있는 경우릐 수로 구해서 O(n*m)으로 구했다

# 또 우유도시 풀면서 느낀게 해당 board판에 0행, 0열을 따로 넣어주면 더 깔끔하게 코드를 짤 수 있는 것 같다

def solution(m, n, puddles):
    answer = 0
    board = [[0]*(m+1) for _ in range(n+1)]
    board[0][1]=1 # 일단 해당 위치 전에 1을 넣어준다
    puddles_set = set(map(tuple,puddles)) # 물웅덩이 위치를 set으로 구해준다
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (j,i) in puddles_set: # 물웅덩이 위치라면 지나친다. 그대로 0으로 둠
                continue
            board[i][j]=board[i-1][j]+board[i][j-1] # 해당 위치로 올 수 있는 위치 두개를 더해준다. 전위치가 물웅덩이라면 0이기때문에 상관없다
    
    answer = board[-1][-1]%1000000007
    return answer

# 22분