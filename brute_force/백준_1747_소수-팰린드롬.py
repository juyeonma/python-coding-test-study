'''
# 백준_1747_소수$팰린드롬. 실버 1. 풀이: 23.05.04

# 풀이방법
- 조건은 3개.
    - 주어진 수보다 크다.
    - 소수이다.
    - 팰린드롬인 수이다.
    
- 소수 판별
: 어떤수의 제곱근을 기준으로 그 왼쪽에 약수가 없다면, 오른쪽에도 없다.

- 풀이
    - 팰린드롬 수 판별과 소수 판별을 각각 함수로 만들어서, 둘다 ok일 경우 출력.
    - 아닐 경우, n += 1

# 반례
1은 팰린드롬 수이지만, 소수가 아니다.
'''

'''
# 보완할 것
- 시간을 더 줄여보자~
    - 맞힌 사람 코드를 보았는데, 기본 로직은 나와 똑같은데, 10배는 빠르다. Why?
'''

# 풀이 기록

# 팰린드롬 판별
def is_palindrome(n):
    if n == n[::-1]:
        return True
    return False

# 소수 판별
def is_prime_num(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False # 소수가 아님
    return True # 소수

n = int(input())

while True:
    if is_palindrome(str(n)) and is_prime_num(n):
        print(n)
        break
    n += 1
    
'''
# 결과
메모리: 31256 KB
시간: 340 ms
코드 길이: 437 B
'''