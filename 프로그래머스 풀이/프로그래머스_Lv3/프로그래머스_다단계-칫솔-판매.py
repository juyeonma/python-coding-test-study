'''
# 프로그래머스_다단계 칫솔 판매. Lv 3. 풀이: 23.06.18

# How to
1번 풀이
- 반례를 고려하지 않음 

2번 풀이
- 1번 풀이와 비슷한데, 반례를 고려
- 판매원: 개수, 조직원: 상사, 조직원: 이익금을 각각 딕셔너리로 만듦
    - 동일 판매원이 여러번 판매할 수 있기 때문에, 판매는 중복 딕셔너리로 담음.

## 반례
seller 에는 같은 이름이 중복해서 들어있을 수 있습니다.

# Review
- 처음에 예시의 그림을 DFS인줄 알았는데, 풀다보니 DP 같은 느낌이 들었다.
- 당연히 맞은줄 알았는데 3, 6번 빼고 틀려서 당황해서 질문게시판을 보니, 문제의 조건에 '중복 허용'을 신경쓰라는 힌트를 보았다.
    - 출처: https://school.programmers.co.kr/questions/25782
- 그 부분을 고려해서 판매원: 개수를 중복 딕셔너리로 만들고, 동일한 개수의 판매를 몇번 했는지를 담았다.
- 역시나 생각하지만, 만약 실전이었다면.. 반례 때문에 실패했을 것이다. 문제를 좀 더 꼼꼼히 보자!

- 다른 사람 풀이를 보니까, 원단위 절사만 생각해서 int(money * 0.1)를 썼는데, 그게 아니라 그냥 moeny // 10을 하면 된다는걸 깨달았다. 왜 생각 못했지..?
'''


# 1. 반례를 생각하지 않았을 때: 3, 6 케이스 빼고 전부 실패
def solution(enroll, referral, seller, amount):
    # 판매원: 금액, 조직원: [이익금, 상사] 각각 딕셔너리
    sell = dict(map(lambda x, y: (x, y*100), seller, amount))
    org = dict(map(lambda x, y: (x, [0, y]), enroll, referral))

    for k in sell:
        money = sell[k]
        person = k
        while person != '-':
            ref_m = int(money * 0.1)
            my_m = money - ref_m
            org[person][0] += my_m
            money = ref_m
            person = org[person][1]

    return [i[0] for i in org.values()]


# 2. 반례를 고려한 풀이: 성공
def solution(enroll, referral, seller, amount):
    # 판매원: 개수를 중복 딕셔너리로 담음.
    sell = {i:{} for i in seller}
    for i, j in zip(seller, amount):
        # 같은 개수를 판매한 횟수를 담음
        if j in sell[i]:
            sell[i][j] += 1
        else:
            sell[i][j] = 1

    # 조직원: 상사 딕셔너리, 조직원: 이익금 딕셔너리
    org = dict(map(lambda x, y: (x, y), enroll, referral))
    answer = {i: 0 for i in enroll}

    # 판매원마다 이익금 분배
    for k in sell:
        for money in sell[k]:
            # 판매 횟수, 현재 분배 대상, 판매금액 지정
            cnt = sell[k][money]
            person = k
            money *= 100
            
            # 가장 정점의 center 직전까지 이익금 분배
            while person != '-':
                # ref_m: 상사에게 올라갈 이익금, my_m: 내가 먹을 이익금
                ref_m = int(money * 0.1)
                my_m = (money - ref_m) * cnt
                
                # 현재 분배 대상의 총 이익금 갱신
                answer[person] += my_m
                # 분배 대상과 남은 금액 갱신
                person, money = org[person], ref_m

    # 조직원 순서대로 총 이익금 return
    return list(answer.values())


'''
# Result
풀이 시간: 1시간
테스트 10 〉통과 (334.55ms, 26.5MB)
'''