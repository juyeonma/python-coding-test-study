def solution(rows, columns, queries):
    answer = []
    gragh=[[0 for i in range(columns+1)] for j in range(rows+1)]
    num=1
    #1부터 1씩 증가하면서 그래프가 채워짐
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            gragh[i][j]=num
            num+=1
    # 4개의 테두리로 나누어서 계산
    for x1,y1,x2,y2 in queries:
        tmp = gragh[x1][y1] #가장 작은 값을 저장
        mini=tmp
        #이동
        for k in range(x1,x2):
            temp=gragh[k+1][y1] #temp에 다음에 이동했을때 기존의 값을 저장
            gragh[k][y1]=temp #저장한 것을 현재위치에 저장
            mini = min(mini,temp) #저장된 값이 최소값이면 저장
        
        for k in range(y1,y2):
            temp=gragh[x2][k+1]
            gragh[x2][k]=temp
            mini = min(mini,temp)
        
        for k in range(x2,x1,-1):
            temp=gragh[k-1][y2]
            gragh[k][y2]=temp
            mini = min(mini,temp)
        
        for k in range(y2,y1,-1):
            temp=gragh[x1][k-1]
            gragh[x1][k]=temp
            mini = min(mini,temp)
        
        gragh[x1][y1+1]=tmp #바뀌지 못한 부분에 처음에 저장한 값을 저장
        answer.append(mini) #최소값만 저장
    return answer