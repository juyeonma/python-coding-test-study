'''
# 백준_ 2671_잠수함식별. 골드 5. 풀이: 23.06.29

# How to
(100~1~|01)~ -> A: 100~1~, B: 01

- 검사할 것:
    - 무조건 시작은 100 or 01, 끝은 1
    - A를 완성할 수 있는가?: A는 1로 끝나야한다.
    - 모든 변환 이후, 0과 1이 남아있으면 안된다.
- A 만들기
    - 100: 100을 A로 바꾸기
    - 100~: A0..을 A로 바꾸기
    - 100~1: A1..을 A로 바꾸기
- B 만들기
    - 01를 B로 바꾸기

## 예제
10010111
-> 1-1. A10111
-> 1-2. A10111
-> 1-3. A0111
-> 2. AB11 
-> 체크 3: NOISE

100000000001101
-> 1-1. A000000001101
-> 1-2. A1101
-> 1-3. A01
-> 2. AB 
-> 체크 3: SUBMARINE


## 다른 사람 풀이: 정규표현식 사용한다면,
- 문제에서 제공된 패턴 ~ 를 + (하나 이상 반복) 으로 바꾼다.
- 길이와 딱 맞게 찾으려면 fullmatch를 사용해야한다.
- match나 search를 사용하면 10011001 일때 10011로 인식이 되어 정확한 답을 내놓지 못한다.
- 출처: https://sinawi.tistory.com/315


## 반례
100 -> 체크 1: NOISE
001 -> 체크 1: NOISE
01100010011001 -> 01AA11001 -> 체크 2: NOISE

# Review
- 반례를 찾느라 대부분의 시간을 허비했다
    - 특히 체크2에서 AA를 늦게 발견했다. 즉 A(100~1~)는 1로 시작해서 1로 끝나야는, AA는 100100 과 같은 형태로, 완전한 A가 아니기 때문에 NOISE가 된다.
- 정규표현식을 사용하지 못해서 그냥 구현했지만, 궁금해서 찾아보니 매우 간단해서 놀랐다.
    - 그러나 시간이 두배 이상 걸렸다.
    - 코테 뿐 아니라 데이터 분석할 때도 정규표현식을 사용하니까, 공부해야겠다..!
'''

# Code
s = input()

# 체크 1: 시작과 끝 검사: 무조건 시작은 100 or 01, 끝은 1
if (s.startswith('100') or s.startswith('01')) and s.endswith('1'):
    # 1-1. A 만들기: 100
    s = s.replace('100', 'A')

    # 1-2. A 만들기: 100~
    while 'A0' in s:
        s = s.replace('A0', 'A')

    # 체크 2: 완성할 수 없는 A 검사: A는 1로 끝나야한다.
    if 'AA' in s:
        print('NOISE')
        
    else:
        # 1-3. A 만들기: 100~1
        while 'A1' in s:
            s = s.replace('A1', 'A')

        # 2. B 만들기: 01
        s = s.replace('01', 'B')

        # 체크 3: 남은 0과 1 검사
        if '0' in s or '1' in s:
            print('NOISE')
            
        else:
            print('SUBMARINE')
        
else:
    print('NOISE')


# 다른 사람 풀이: 정규표현식 사용한다면, 34804 KB, 112 ms
## 1. 출처: https://velog.io/@youngcheon/백준-2671-잠수함-식별-Python-정규표현식
import re
print(re.fullmatch('(100+1+|01)+', input()) and "SUBMARINE" or "NOISE")

## 2.  출처: https://sinawi.tistory.com/315
import re
p = re.compile('(100+1+|01)+')
m = p.fullmatch(input())
if m:
    print("SUBMARINE")
else:
    print("NOISE")
    
    
'''
# Result
풀이 시간: 1시간
메모리: 31256 KB
시간: 40 ms
코드 길이: 784 B
'''