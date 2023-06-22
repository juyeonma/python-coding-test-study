#누적합,,?
#다시 이해하기,,
def solution(board, skill):
    answer = 0
    gragh = [[0 for j in range(len(board[0])+1)] for i in range(len(board)+1)]
    for t,r1,c1,r2,c2,d in skill:
        if t==2:
            d=-d
        #누적합 계산
        gragh[r1][c1] -=d
        gragh[r1][c2+1]+=d
        gragh[r2+1][c1]+=d
        gragh[r2+1][c2+1]-=d
        
    for i in range(len(gragh)-1):
        for j in range(len(gragh[0])-1):
            gragh[i][j+1]+=gragh[i][j]
    for i in range(len(gragh)-1):
        for j in range(len(gragh[0])-1):
            gragh[i+1][j]+=gragh[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]+gragh[i][j]>0:
                answer+=1
    return answer