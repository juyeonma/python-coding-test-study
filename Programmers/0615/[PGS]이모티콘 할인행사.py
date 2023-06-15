# 알고리즘 : 구현..?
# 풀이시간 : 1시간 + @
# 못 풀었다.. => 지문부터 제대로 안 봐서 꼬인 것 같다..
# 이모티콘 상품 각각 할인율을 제대로 파악하지 못했었다..

# 참고 : https://magentino.tistory.com/59
# 핵심
# 1. 구매자 n명은 각자 기준 할인율이 있고,
# 2. 이모티콘 상품 m개는 각각 할인율을 10%, 20%, 30%, 40% 설정 가능하며
# 3. 구매자는 기준 할인율보다 더 높은 할인율 이모티콘을 전부 구매하며
# 4. 만약 이렇게 구매한 이모티콘 총 가격이 구매자의 기준 금액 이상이면 구매 대신 이모티콘 플러스를 가입한다.
# 풀이 참고 : https://velog.io/@dh1010a/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4150368-%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98-%ED%95%A0%EC%9D%B8%ED%96%89%EC%82%AC
# 접근 방법 : dfs
# 아직 dfs 풀이를 봐도 바로 바로 이해가 가지는 않는 것 같다.
# 조금 더 노력해봐야겠다...
def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discount = []
    def dfs(tmp, d): # 모든 경우의 할인율 조합을 구함
        if d == len(tmp):
            discount.append(tmp[:])
            return
        else:
            for i in data:
                tmp[d] += i
                dfs(tmp, d+1)
                tmp[d] -= i
    dfs([0]*len(emoticons), 0)
    
    for disc in discount: # 만들어진 모든 조합을 하나씩 살펴봄
        cnt = 0
        get = 0
        for i in users:
            pay = 0
            for j in range(len(disc)):
                if i[0] <= disc[j]:
                    pay += emoticons[j] * (100 - disc[j])/100
                if pay >= i[1]:
                    break
            if pay >= i[1]: # 만약 유저의 제한금액 초과시 플러스 구매
                pay = 0
                cnt += 1
            get += pay
        if cnt >= answer[0]: # 현재 최대값을 넘어가면 갱신
            if cnt == answer[0]:
                answer[1] = max(answer[1], get)
            else:
                answer[1] = get
            answer[0] = cnt

    return answer