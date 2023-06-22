# 이중 포문이면 효율성 테스트에서 탈락일줄 알았는데.. 통과였다..
# 심지어 생각보다 오래 걸리지도 않았다..
def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                count = j - i
            else:
                count = j - i
                break
        answer.append(count)
    return answer

# 시간
# 효율성 테스트
# 테스트 3 〉	통과 (171.03ms, 19.4MB)
# 테스트 5 〉	통과 (74.43ms, 17MB)

# deque를 활용해서 풀었어야 했나보다..!
# deque 활용하기
# 참고 : https://school.programmers.co.kr/learn/courses/30/lessons/42584/solution_groups?language=python3
from collections import deque
def solution(prices):
    answer = []
    dq = deque(prices)
    while dq:
        price = dq.popleft()

        count = 0
        for i in dq:
            if price > i:
                count += 1
                break
            count += 1
        
        answer.append(count)
    return answer

# 속도가 훨씬 줄았다는 것을 알 수 있다.
# 효율성 테스트
# 테스트 3 〉	통과 (75.29ms, 19.5MB)
# 테스트 5 〉	통과 (36.05ms, 16.8MB)