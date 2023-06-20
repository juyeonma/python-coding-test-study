'''
# 프로그래머스_92335_k진수에서 소수 개수 구하기. Lv 2. 풀이: 23.06.13

# How to
- n을 k진법으로 나타낸다
    - n을 계속 n // k로 갱신하면서 n % k를 앞에 더해준다. n이 0이되면, 멈춘다.
- 조건에 0을 사이에 두고 수가 존재해야 하기 때문에, 0을 기준으로 split한 list를 만든다.
- list의 원소들 중 소수의 개수를 센다.


# Review
- 소수 판별 시, 탐색 범위를 제곱근까지 하지 않으면 1번 테스트 케이스에서 시간초과가 뜬다.
- n을 k진수로 바꾸는 함수를 몰라서 직접 구현했는데, 풀고나서 찾아보니 그런 함수는 없었다.
    - k진수를 10진수로 바꾸는 함수는 존재: int('n', k)
    - 10진수를 2, 8, 16진수로 바꾸는 함수도 존재: 각각 bin(n), oct(n), hex(n)
'''

# 1. Code
# 소수 판별 함수
def prime_num(n):
    # 빈 문자열: 제거, 1: 소수가 아님
    if n in ['', '1']:
        return False
    
    n = int(n)
    # 제곱근까지 탐색(제곱근을 기준으로 약수들이 대칭되니까)
    for i in range(2, int(n**(1/2)+1)):
        if not n % i:
            return False
    return True

def solution(n, k):
    # k진수 만들기
    num = ''
    while n:
        n, b = n // k, n % k
        num = str(b) + num

    # 0을 기준으로 split하여 list로 만듦
    arr = num.split('0')
    answer = 0
    for i in arr:
        # 소수의 개수 세기
        if prime_num(i):
            answer += 1

    return answer


'''
# Result
풀이 시간: 30분
테스트 1 〉통과 (90.60ms, 10.4MB)
'''