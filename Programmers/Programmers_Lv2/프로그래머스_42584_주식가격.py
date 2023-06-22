'''
# 프로그래머스_42584_주식가격. Lv 2. 풀이: 23.06.22 -> 실패 -> 성공

# How to
## 1. 완전탐색으로 풀기 -> 시간초과
## 2. 최대힙 사용 -> 성공
- 가격이 떨어지면, 큐의 원소들과 반복해서 비교
    - 가격이 높은 것부터 비교
    - 가격이 떨어졌다면, 인덱스 차이 만큼 정답에 추가
    - 가격이 떨어지지 않았다면, 다시 큐에 넣고 break
- 큐에 원소 추가: 가격이 높은 것부터 비교하기 위해서 최대힙 사용
- 끝까지 가격이 떨어지지 않은게 있다면, 남은 인덱스-1 만큼 정답에 추가


# Review
- 처음에 완전탐색으로 했다가, 역시 시간초과가 나서 질문게시판을 보았다.
- 스택으로 푸는 힌트였는데, 최대힙이 더 낫지 않을까? 싶어서 최대힙으로 성공..
    - 출처: https://school.programmers.co.kr/questions/41439
    
- 그런데 다른 사람 풀이를 보니, 스택 풀이가 가능했고, 심지어 더 빨랐다.   
- 여전히 스택과 큐를 자유자재로 다루는게 쉽지 않게 느껴진다.. 
'''

# 1. 시간초과 Code
## 정확성 테스트 5 〉통과 (50.09ms, 10.3MB), 효율성 테스트: 실패
def solution(prices):
    n = len(prices)
    answer = [n-i-1 for i in range(n)]
    check = [True if 1 < i else False for i in prices]
    
    for i, v in enumerate(prices):
        for j in range(i):
            if v < prices[j] and check[j]:
                check[j] = False
                answer[j] = i-j

    return answer


# 2. 최대힙 사용: 성공
## 정확성 테스트 10 〉통과 (1.07ms, 10.3MB), 효율성 테스트 3 〉통과 (85.39ms, 19.6MB)
import heapq

def solution(prices):
    n = len(prices)
    answer = [0] * n
    q = []
    before = 0
    for i, v in enumerate(prices):
        # 가격이 떨어졌다면
        if v < before:
            while q:
                v2, i2 = heapq.heappop(q)
                # 가격이 떨어지지 않았다면, 다시 큐에 넣고 break
                if -v2 <= v:
                    heapq.heappush(q, (v2, i2))
                    break  
                # 가격이 떨어졌다면, 인덱스 차이 만큼 정답에 추가
                answer[i2] = i-i2

        heapq.heappush(q, (-v, i))
        before = v
    
    # 끝까지 가격이 떨어지지 않은게 있다면, 남은 인덱스-1 만큼 정답에 추가
    while q:
        v2, i2 = heapq.heappop(q)
        answer[i2] = n-i2-1

    return answer


# 다른 사람 풀이
# 1. 스택 이용(일부 불필요한 부분 수정): 효율성 테스트 3 〉통과 (29.31ms, 19.4MB)
def solution(prices):
    n = len(prices)
    stack = []
    answer = [0] * n
    for i, v in enumerate(prices):
        while stack and v < stack[-1][1]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, v])
        
    for i, _ in stack:
        answer[i] = n - 1 - i
        
    return answer


# 2. 스택 사용: 효율성 테스트 3 〉통과 (56.48ms, 19.5MB)
def solution(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans


# 3. deque 사용: 효율성 테스트 3 〉통과 (81.69ms, 19.5MB)
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()
        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1
        answer.append(count)

    return answer


'''
# Result
풀이 시간: 30분

'''