'''
# 프로그래머스_12946_하노이의 탑. Lv 2. 풀이: 23.06.06

# How to
- 이동 횟수: 2**n - 1
- 이전 단계의 값을 가져오는데..
    기둥이 a, b, c 라고 하면,
    - n-1에서 짝수 index: [a, b]
    -> n: [a, c], [a, b], [c, b] (c: a, b가 아닌 나머지 기둥)

    - n-1에서 홀수 index: [a, b]
    -> n: [a, b]

##예제
n: 정답
1: [[1,3]]
2: [[1,2], [1,3], [2,3]]
3: [[1,3], [1,2], [3,2], [1,3], [2,1], [2,3], [1,3]]
4: [[1,2], [1,3], [2,3], [1,2], [3,1], [3,2], [1,2], [1,3], [2,3], [2,1], [3,1], [2,3], [1,2], [1,3], [2,3]]


# Review
- 난 당연히 dp인줄 알았는데.. 검색해보니 재귀호출의 가장 유명한 예시라고 한다.
    - 코드도 보니까 엄청 간단함..ㅎ..
- 여튼 규칙이 있길래 풀었으니 괜찮은거 아닐까..?
'''

# Code
# Bottom-up code
## 1. 홀수와 짝수 index를 나누어서 추가
def solution(n):    
    # 1+2=3, 1+3=4, 2+3=5
    idx = [1,2,3,3,2,1]
    dp = [[1, 3]]
    
    for i in range(1, n):
        tmp = []
        # 홀수 여부 -> 짝수라 False로 시작
        odd = False
        for j in range(2**i-1):
            # 매번 j % 2 로 홀짝 판단해도 됨: 시간은 비슷함
            if odd: # 홀수 index
                tmp.append(dp[j])
                odd = False
                
            else: # 짝수 index 
                a, b = dp[j]
                c = idx[a+b]
                tmp.extend([[a, c], [a, b], [c, b]])
                odd = True

        # 새로운 dp로 갱신
        dp = tmp

    return dp
'''
테스트 13 〉	통과 (9.95ms, 18.9MB)
'''

## 2. 먼저 dp를 만들고, 짝수와 홀수 인덱스일때 dp 갱신 -> 더 오래걸림
def solution(n):    
    # 1+2=3, 1+3=4, 2+3=5
    idx = [1,2,3,3,2,1]
    dp = [[1, 3]]
    
    for i in range(1, n):
        now = 2**i - 1
        tmp = [[0, 0] for _ in range(now*2 + 1)]

        # 홀수 index
        for j in range(1, now, 2):
            tmp[j*2 + 1] = dp[j]
            
        # 짝수 index
        for j in range(0, now, 2):
            next = j*2 + 1
            a, b = dp[j]
            c = idx[a+b]
            tmp[next-1], tmp[next], tmp[next+1] = [a, c], [a, b], [c, b]
            
        # 새로운 dp로 갱신
        dp = tmp

    return dp

'''
테스트 13 〉	통과 (39.78ms, 19.1MB)
'''

# Top-down Code -> 실패: 시간초과
def solution(n):    
    # 0(index가 0부터 시작해서), 1, 2
    dp = [[[0,0]], [[1, 3]], [[1,2], [1,3], [2,3]]]
    for _ in range(3, n+1):
        tmp = [[0, 0] for _ in range(2**n - 1)]
        dp.append(tmp)
    
    # 1+2=3, 1+3=4, 2+3=5
    idx = [1,2,3,3,2,1]
    
    def top_down(n):
        
        if [0, 0] not in dp[n]:
            return dp[n]
        
        now = 2**n -1
        
        for i in range(1, now, 4):
            dp[n][i] = top_down(n-1)[(i-1)//2]
            
            a, b = dp[n][i]
            c = idx[a+b]
            dp[n][i-1], dp[n][i+1] = [a, c], [c, b]
            
        for i in range(3, now, 4):
            dp[n][i] = top_down(n-1)[(i-1)//2]
        
        return dp[n]

    return top_down(n)


'''
# Result
풀이 시간: 1시간
테스트 13 〉	통과 (9.95ms, 18.9MB)
'''