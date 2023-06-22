from itertools import combinations
def solution(relation):
    answer = 0
    row=len(relation)
    col = len(relation[0])
    can = []
    for i in range(1,col+1):
        can.extend(combinations(range(col),i)) #조합만들기
    #extend는 append와 다르게 다양한 요소를 추가
    #유일성
    uni=[]
    for c in can:
        tmp = [tuple([item[i] for i in c]) for item in relation] #전체 관계에서 조합들을 비교해서 튜플을 만듬
        if len(set(tmp))==row: #그렇게 만든 조합들이 전체 행 개수와 동일한지
            uni.append(c) #그 조합을 저장
            
    #최소성(유일성을 만족하는 것중에)
    answer=set(uni)
    for i in range(len(uni)): #유일성을 만족하는 조합들을 비교
        for j in range(i+1,len(uni)):
            if len(uni[i])==len(set(uni[i])&set(uni[j])): #길이가 같으면 겹치는 것
                answer.discard(uni[j]) #삭제
                    
    return len(answer)