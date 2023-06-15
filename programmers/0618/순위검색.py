def solution(info, query):
    answer = []
    for q in query:
        q=q.replace("and","") #and를 제거하고 공백을 기준으로 나눈다
        q=q.split()
        cnt=0
        for i in info:
            i=i.split()
            flag=True
            if int(i[4])<int(q[4]): #점수가 조건을 만족하지 않으면 실패
                flag = False
            else:
                for j in range(4):
                    if q[j]=="-": #-는 고려하지 않는다는 의미로 패스
                        continue
                    else: #-를 제외한 모든 선택지들 중에서
                        if q[j]!=i[j]: #q와 i가 다르다면
                            flag=False #false
                            break
            if flag: #1개의 쿼리에 대해서 1개의 info를 탐색했을 때 조건에 맞다면
                cnt+=1 #cnt 증가시키고
        answer.append(cnt) #결과답에 저장
    return answer

#효율성테스트는 실패