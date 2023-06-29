# 유형 : 구현..? => 구현인줄 알았는데 정렬이었다..

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(citations[0], -1, -1):
        count = 0
        for j in citations:
            if i <= j:
                count += 1
        if count >= i:
            answer = i
            break
    
    return answer
solution([3, 0, 6, 1, 5])
# 속도
# 테스트 15 〉	통과 (328.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)

# 이중 포문이 아닌 for문 하나로 끝나는 풀이
# 참고 : https://school.programmers.co.kr/learn/courses/30/lessons/42747/solution_groups?language=python3
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
solution([3, 0, 6, 1, 5])
# 속도
# 테스트 15 〉	통과 (0.11ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)