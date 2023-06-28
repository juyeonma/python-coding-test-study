def solution(m, n, puddles):
    answer = 0
    gragh = [[0] * (m+1) for _ in range(n+1)]
    gragh[1][1]=1
    #DP로 풀음
    for i in range(1,n+1):
        for j in range(1,m+1):
            if gragh[i][j]==1:
                continue
            if [j,i] in puddles:
                gragh[i][j]=0 #웅덩이는 이동 횟수가 없으므로 0
            else:
                gragh[i][j]=gragh[i-1][j]+gragh[i][j-1] #이동 가능 방향에서 합침
            
    answer = gragh[n][m]%1000000007
    return answer

print(solution(4,3,[[2, 2]]))