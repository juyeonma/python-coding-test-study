'''
# 프로그래머스_스티커 모으기(2). Lv 3. 풀이: 23.06.09 -> 실패

# How to
## 1. 실패한 풀이
- DP 점화식: dp[n] = max(dp[n-3], dp[n-2]) + dp[n]
- n-1은 뗄 수 없으니, n-3과 n-2 중 큰 값에다가 n의 스티커값을 더하려고 했다.


## 2. 다른 사람 풀이(검색)
- 참고: https://latte-is-horse.tistory.com/231
- DP 점화식: n번째 index까지 최대 점수
    - dp[n] = max(dp[n-2]+sticker[n], dp[n-1])
- 첫번째 스티커를 뜯는다면, 
    - dp[0], dp[1] 은 첫번째 스티커 점수
    - 마지막 스티커는 탐색에서 제외
- 첫번째 스티커를 뜯지 않는다면,
    - dp[0]은 0, dp[1]은 두번째 스티커 점수.
    
    
# Review
- 전형적인 DP 문제였지만..역시나 너무 어려운 DP. 실패했다.
- 백준에서 풀었던 2행짜리 스티커 떼기와 비슷한줄 알았는데, 약간 달랐다.
- 실패한 내 코드에서는 스티커의 개수에 따라 3~6까지 나누었다.
    - 그러나 원형으로 연속되어 있기 때문에 중복으로 점수가 더해지는 문제가 발생해서, 실패
- 검색해보니, '첫번째 스티커'가 포인트였다.
    - 즉, 아무리 원형으로 연속되었다고 할지라도, 첫번째 스티커를 떼냐 안 떼냐의 두 갈림길이 있을 뿐이다.
'''


# 실패 Code
def solution(sticker):
    answer = 0
    n = len(sticker)
    # 스티커가 3개라면: 2 / 0 1 2 / 0 => 하나를 붙이면, 나머지 두개를 붙일 수 없음.
    if n <= 3:
        return max(sticker)
    elif n == 4:
        return max(sticker[0]+sticker[2], sticker[1]+sticker[3])
    elif n == 5:
        for i in range(n):
            answer = max(answer, max(sticker[i-3], sticker[i-2]) + sticker[i])
        return answer
    else: # 스티커 개수가 6 이상일 때
        dp = [0] * n
        dp_idx = [[] for _ in range(n)]
        
        for i in range(n):
            a, b = (i-3)%n, (i-2)%n
            no1, no2 = (i-1)%n, (i+1)%n
            
            j = a
            if dp[a] < dp[b]:
                j = b

            if no1 not in dp_idx[j] and no2 not in dp_idx[j]:
                dp_idx[i].extend(dp_idx[j])
                dp_idx[i].append(j)     

                if i in dp_idx[j]:
                    dp[i] = dp[j]
                else:
                    dp[i] = dp[j] + sticker[i]

        return max(dp)


# 다른 사람 코드: 효율성 테스트 4 〉통과 (64.85ms, 17.4MB)
def solution(sticker):
    if len(sticker)==1: return sticker[0]
    
    d1, d2 = [0] * len(sticker), [0] * len(sticker)
    
    # d1은 맨 앞 뜯는 경우: 0번은 뜯었으니, 1번은 못 뜯고, 2번~n-2까지 탐색
    d1[0], d1[1] = sticker[0], sticker[0]
    for i in range(2, len(sticker)-1):
        d1[i] = max(d1[i-2]+sticker[i], d1[i-1])
    
    # d2는 맨 앞 뜯지 않는 경우: 그냥 그대로 쭉 dp 값 구하기
    for i in range(1, len(sticker)):
        d2[i] = max(d2[i-2]+sticker[i], d2[i-1])

    return max(d1[-2], d2[-1])


# 변형: 위의 다른 사람 코드를 보고 나서, 중복되는 부분을 따로 함수로 빼봤다.
## 효율성 테스트 4 〉통과 (68.80ms, 14.2MB)
def make_dp(sticker, a, b, end):
    dp = [0] * len(sticker)
    dp[0], dp[1] = a, b
    
    # dp1이라면, 마지막 스티커는 제외(len(sticker) - 1)
    for i in range(2, len(sticker)-end):
        dp[i] = max(dp[i-2]+sticker[i], dp[i-1])
        
    # 마찬가지로 dp1이라면, dp[-2]를 return 하게 된다.
    return dp[-1-end]

def solution(sticker):
    if len(sticker)==1: 
        return sticker[0]
    
    # dp1: 첫번째 스티커를 뜯음. dp2: 첫번째 스티커를 뜯지 않음
    dp1 = make_dp(sticker, sticker[0], sticker[0], 1)
    dp2 = make_dp(sticker, 0, sticker[1], 0)

    return max(dp1, dp2)


'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''