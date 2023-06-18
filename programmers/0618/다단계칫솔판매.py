def solution(enroll, referral, seller, amount):
    answer = []
    coin = [0 for _ in range(len(enroll))]
    dict = {}
    
    for i, e in enumerate(enroll): #등록자들을dic에 다 넣음(인덱스를 붙여서)
        dict[e] = i
    for s,a in zip(seller,amount): #셀러와 판매개수을 하나로 묶어서 계산
        m=a*100 #칫솔을 1개당 100원
        while s!="-" and m>0: #추천인이 없어지거나 이익금이 0이 되는 순간 종료
            idx=dict[s] #인덱스에 딕셔너리의 셀러의 인덱스를 저장
            coin[idx] += m-m//10 #이익금 계산하고 추천인에게 준 금액을 뺸 것을 저장
            m//=10 
            s=referral[idx] #셀러는 현재 판매자의 추천인으로 저장
    return coin