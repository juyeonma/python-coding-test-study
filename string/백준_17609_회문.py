'''
# 백준_17609_회문. 골드 5. 풀이: 23.06.29

# How to
- 0: 회문, 1: 유사회문, 2: 일반 문자열

- 문자열 = 뒤집은 문자열이라면, 0 반환(회문)
- 회문이 아닌데, 
    - 유사회문 판단중이라면 -> 바로 2 반환(일반 문자열)
    - 원래 문자열이라면, 유사회문 판단 들어감
- 유사회문 판단: 양끝에서 하나씩 문자열 비교
    - 다른 문자열일 경우, 왼쪽과 오른쪽 각각 하나씩 문자열을 제거한 후 회문인지 판단
    - 하나라도 회문이라면, 1 반환(유사회문)
    - 둘다 회문이 아니라면, 2 반환(일반 문자열)


## 반례
5
abbab
aapqbcbqpqaa
axaaxaa
aaab
zabcczba
답:
1
1
1
1
2 -> 회문이 되려면 2개를 삭제해야함


# Review
- 반례에서 고생했다.
    - pq와 qpq처럼, q를 제거하느냐 p를 제거하느냐에 따라 유사회문이 되거나, 일반 문자열이 된다.
- 결국 유사회문 판단을 위해서, 하나씩 양끝에서 제거 후 재귀로 한번 들어갔다.
'''

# Code
def solve(s, pseudo_palindrome):
    # 0: 회문
    if s == s[::-1]:
        return 0
    
    # 이미 유사회문 판단중인데, 회문이 아닐 경우 -> 2: 일반 문자열
    if pseudo_palindrome:
        return 2
    
    # 1: 유사회문 판단
    left, right = 0, len(s)-1
    while left <= right:
        if s[left] != s[right]:
            # s[left] 제거, s[right] 제거
            # 제거 후 회문이라면(하나라도 0이면) -> 1: 유사회문
            if not solve(s[left+1:right+1], True) or not solve(s[left:right], True):
                return 1
            
            # 제거 후 회문이 아니라면(둘다 0이 아니면) -> 2: 일반 문자열
            return 2

        left += 1
        right -= 1

for _ in range(int(input())):
    print(solve(input(), False))


'''
# Result
풀이 시간: 1시간
메모리: 31256 KB
시간: 116 ms
코드 길이: 818 B
'''
