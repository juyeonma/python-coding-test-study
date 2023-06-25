def solution(genres, plays):
    answer = []
    temp = []
    total = {}
    temp = [[genres[i],plays[i], i] for i in range(len(genres))]
    temp = sorted(temp,key=lambda x:(x[0],-x[1],x[2]))
    
    for i in temp:
        if i[0] not in total: #장르가 전체 딕셔너리에 없을때
            total[i[0]] = i[1] #새로 추가
        else:
            total[i[0]] += i[1] #있으면 있던 재생횟수에 추가
    total = sorted(total.items(),key=lambda x:-x[1]) #재생횟수가 많은 순으로 정렬
    
    for i in total: 
        cnt=0
        for j in temp:
            if i[0]==j[0]: #전체하고 재생횟수 딕셔너리에서 장르가 같으면
                cnt+=1 #개수 세기
                if cnt>2: #2개씩 묶는다고 했으므로 그 이상이 되면 종료
                    break
                else:
                    answer.append(j[2]) #고유번호를 추가
    return answer