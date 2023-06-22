from itertools import product
def solution(users, emoticons):
    answer = []
    sale=[10,20,30,40] #0.1 이런식으로 바꾸니까 결과값이 소수점으로 나옴
    
    for case in product(sale,repeat=len(emoticons)): 
        #중복조합 함수 : 조합할 데이터를 넣고, repeat를 통해 몇개의 데이터를 뽑을지 정함
        #print(case)
        result=[0,0]
        for user in users:
            temp = 0
            for idx,sales in enumerate(case):
                #print(idx,sales)
                if sales>=user[0]: #조합에 있는 할인율이 사용자가 원하는 할인율 이상이라면
                    temp += emoticons[idx]*(100-sales)//100
                #print(temp)
            if temp >= user[1]: #이모티콘 총 구매 가격이 원래 금액보다 비싸다면
                result[0]+=1 #이모티콘 플러스 구매 개수 증가
            else:
                result[1]+=temp #가격을 증가
        answer.append(result)
    answer.sort(key=lambda x:(-x[0],-x[1]))  #max로 구할수 없는 리스트이므로 sort사용
    return answer[0] #0번 인덱스에 조건을 만족하는 최대값이 정렬되므로

a = [[40, 10000], [25, 10000]]
b=[7000, 9000]
print(solution(a,b))