'''
# 프로그래머스_150368_이모티콘 할인행사. Lv 2. 풀이: 23.06.15 -> 실패 -> 검색 후 성공

# How to을
- 적정한 할인율은 뭘까?
할인을 너무 작게 하면, 이모티콘을 안 산다 -> 이모티콘 플러스 가입 X, 구매 비용 증가 X
할인을 너무 많이 하면, 이모티콘을 다 산다 -> 구매 비용은 줄어들고, 이모티콘 플러스 가입도 안 할 확율이 늘어난다.

- 모든 이모티콘에 대해 중복순열을 구해서, 전부 탐색한다.
    - 모든 사용자에 대해 상한비율과 상한가격 조건을 따져보고, 
    - 가입자가 최대가 되도록 갱신한다.


# Review
- 처음에 permutations를 쓰는 바람에 일부 케이스만 통과했다.
- 그래서 검색하니까, product를 써야한다는걸 알게 되고, 중복순열로 푸니까 바로 통과했다.
- 특별한 로직이 있는건 아니고, 그냥 완전탐색이었다.
    - 시간 복잡도 팁: https://school.programmers.co.kr/questions/43408
- 먼저 할인이 적용된 이모티콘 가격을 구한 뒤 사용자를 탐색했는데,
    매 사용자마다 상한가격 이상일 때 이모티콘 할인가를 계산해도 된다. 다만 조금 시간이 더 걸릴지도?
- 퍼센트를 곱셈할 때 조금 더 편하게 하려고 딕셔너리를 사용했다.
- 가입자 갱신 시, list는 어떻게 max가 적용되는지 몰라서 조건문으로 해봤다가, 그냥 max를 써도 된다는걸 깨달았다.
'''


# 1. 성공
## 테스트 13 〉통과 (724.69ms, 11.6MB)
from itertools import product

def solution(users, emoticons):
    m = len(emoticons)
    dic = {10: 0.9, 20: 0.8, 30: 0.7, 40: 0.6}
    idx = list(product((10, 20, 30, 40), repeat=m))

    answer = [0, 0]
    for arr in idx:
        # 할인율, 할인가 순서로
        emo = list(map(lambda x, y: (x, dic[x]*y), arr, emoticons))
        people, money = 0, 0
        # 각각의 사용자에 대하여,
        for rate, price in users:
            cost = 0
            # 각 이모티콘을 구매할지 말지,
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
                
        # 가입자 갱신    
        answer = max(answer, [people, money])
            
    return answer


'''
# Result
풀이 시간:

'''