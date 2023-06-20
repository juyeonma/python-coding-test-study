'''
# 프로그래머스_138476_귤 고르기. Lv 2. 풀이: 23.06.13

# How to
- 개수가 많은 귤의 종류를 골라야한다.
- 종류를 key로, 개수를 value로 해서 dictionary에 넣는다.
- value만 뽑아서 내림차순 정렬 후, 차례대로 더한다.
    - 더한 값이 k 이상이 되는 순간 그때까지의 종류의 수가 곧 정답

# Review
- 처음에는 딕셔너리 만들때 count을 쓸까 하다가..매번 O(n)이 걸릴테니, 일일히 for문을 돌렸다.
    - 역시나 count로 하면 시간초과가 뜨더라.
'''

# 1. 성공
def solution(k, tangerine):
    # count를 사용하면 시간초과:
    # dic = {i: tangerine.count(i) for i in set(tangerine)}
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    # value만 뽑아서 내림차순 정렬
    dic = sorted(dic.values(), reverse=True)

    # 차례대로 귤의 개수를 더했을 때 k 이상이 된다면, 그때까지의 종류의 수가 곧 정답
    idx = 0
    while k > 0:
        k -= dic[idx]
        idx += 1
        
    return idx


'''
# Result
풀이 시간: 15분
테스트 29 〉통과 (51.05ms, 18.1MB)
'''