'''
# 프로그래머스_이모티콘 할인행사. Lv 2. 풀이: 23.06.15 -> 실패

# How to
- 적정한 할인율을 정해야한다.
할인을 너무 작게 하면, 이모티콘을 안 산다 -> 이모티콘 플러스 가입 X, 구매 비용 증가 X
할인을 너무 많이 하면, 이모티콘을 다 산다 -> 구매 비용은 줄어들고, 이모티콘 플러스 가입도 안 할 확율이 늘어난다.

- 모든 이모티콘에 대해 가능한 할인율의 순열을 구해서, 전부 탐색한다.
    - 가입이 최대가 되도록 갱신



# Review
- 오래 걸릴거 같긴 했는데, 여기서 어떻게 개선해서 시간초과를 해결해야할지 모르겠다..
'''

# 1. 시간초과 Code: 합계: 55.0 / 100.0
from itertools import permutations

def solution(users, emoticons):
    m = len(emoticons)
    dic = {10: 0.9, 20: 0.8, 30: 0.7, 40: 0.6}
    permuts = []
    # 가능한 할인율의 순열 만들기
    for i in range(10, 50, 10):
        permuts += [i] * m

    answer = [0, 0]
    for arr in list(permutations(permuts, m)):
        # 할인율, 할인가 순서로 list
        emo = list(map(lambda x, y: (x, dic[x]*y), arr, emoticons))
        people, money = 0, 0
        for rate, price in users:
            cost = 0
            for r, p in emo:
                # 상한비율보다 할인율이 높으면, 이모티콘 구매
                if rate <= r:
                    cost += p
            # 상한가격보다 구매가가 높을경우, 구매 취소 후 서비스 가입
            if price <= cost:
                people += 1
            # 상한가격보다 구매가가 낮을 경우, 이모티콘 구매 확정
            else:
                money += cost       
                
        # 가입자가 많도록 갱신    
        if answer[0] < people:
            answer = [people, money]
        elif answer[0] == people:
            answer[1] = max(answer[1], money)
            
    return answer

'''
# Result
풀이 시간:

'''