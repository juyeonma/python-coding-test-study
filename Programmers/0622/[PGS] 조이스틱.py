# 유형 : 구현..?

# 실패 : 11, 13, 14, 18, 20, 22 ~ 27
# 채점 결과
# 정확성: 59.3
# 합계: 59.3 / 100.0

# 실패인 이유
# 한쪽 방향으로만 계속 움직이는 경우만 구했음..
def solution(name):
    answer = ['A'] * len(name)
    name = list(name)
    left = 0
    right = 0
    for i in range(len(name)):
        n = name[i]
        left += min(ord(n) - ord('A'), ord('Z') - ord(n)+1)
        answer[i] = n
        if answer == name:
            break
        left += 1
    answer = ['A'] * len(name)
    for i in range(0, -len(name), -1):
        n = name[i]
        right += min(ord(n) - ord('A'), ord('Z') - ord(n)+1)
        answer[i] = n
        if answer == name:
            break
        right += 1
    return min(left, right)

# 통과하지 못한 예외 케이스 예시들(참고 : https://school.programmers.co.kr/questions/25695)
# solution("ABAAAAAAAAABB") // 7
# solution("BBBBAAAAAB"); // 10

# 결국 참고 : https://bellog.tistory.com/152
def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1
    
    if (min_move < 0):
        return answer
        
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, i + (i + len(name)) - next)
    answer += min_move
    return answer

solution("ABAAAAAAAAABB")