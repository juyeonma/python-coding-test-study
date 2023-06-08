'''
# 프로그래머스_[1차] 뉴스 클러스터링.py. Lv 2. 풀이: 23.06.08

# How to
- 처음에 1번 방법으로 풀고, 나중에 2, 3 으로도 풀어봄.
- 영문자 판별: isalpha()보다 a in b 방법(etc로)이 더 빠름. re 정규식도 느림.
- 중복 원소 개수: count 보다 dictionary가 더 빠름. 혹은 직접 집합 구하기.

## 1. 원소 list, dictionary로 중복 세기, etc로 영문자 판별
- 중복도 세기 때문에, 딕셔너리로 중복의 개수를 세야한다.
- 소문자로 변환: lower()
- 공백이나 숫자, 특수 문자는 제거: etc(숫자+특수문자+공백)에 있는지 판별

- 교집합: A와 B의 딕셔너리에 있다면, 최솟값을 더해서 교집합의 길이를 구한다.
- 합집합: A와 B의 딕셔너리에 있다면, 최댓값을 더해서 합집합의 길이를 구한다.
- 최종적으로 자카드 유사도에 65536을 곱한 후 정수로 반환한다.

## 2. isalpha, count 사용: 코드가 더 느려짐
- isalpha(): 영문자 판별
- 교집합, 합집합의 각 원소가 A와 B list에서 각각 몇개인지: count 사용

## 3. 중복교집합, 중복합집합 직접 구하기
- list를 복사해서, 넣고 빼면서 구함.
- 중복교집합의 길이, 중복합집합의 길이로 최종적으로 유사도 계산


# Review
- 처음에 1번 방법으로 풀고, 나중에 2, 3 으로도 풀어봤다.
    - re 정규식을 사용해도 되는데, 사용이 가능한지 잘 몰라서 그냥 함수로 만들었다.
    - 근데 특수문자가 저게 다인가..? 더 있는지 모르겠지만, 여튼 통과됨.
- 다른 사람 풀이를 보니, isalpha, count, re, Counter 등 다양하게 사용했다.
    - 그러면 코드가 더 간단하고 짧아지지만, 그게 더 빠른 코드는 아니었다. 그래도 Counter 사용한 코드는 깔끔하고 빠르기에, 나중에 공부해야겠다.
    - 영문자 판별: isalpha()보다 a in b 방법(etc로)이 더 빠름. re 정규식도 느림.
    - 중복 원소 개수: count 보다 dictionary가 더 빠름. 혹은 직접 집합 구하기.
'''

# 1. 처음 성공 Code: 처음에는 영문자 판별도 따로 함수로 했는데, 포함한 버전
# 2개씩 끊은 문자열 list와 중복 갯수를 셀 dictionary 만들기
def make_arr(s, etc):
    l, d = [], {}
    s = str.lower(s)
    for i in range(len(s)-1):
        # 영문자만 존재하는 경우,
        if s[i] not in etc and s[i+1] not in etc:
            tmp = s[i:i+2]
            l.append(tmp)
            if tmp in d:
                d[tmp] += 1
            else:
                d[tmp] = 1
    return l, d

def solution(str1, str2):
    etc = "1234567890!@#$%^&*()-_+=[]{}<>?/\|,.;:~` "
    list1, dic1 = make_arr(str1, etc)
    list2, dic2 = make_arr(str2, etc)
    
    # 집합 A와 집합 B가 모두 공집합일 경우, 유사도는 1
    if not list1 and not list2:
        return 65536
    
    a, b = 0, 0
    # 교집합의 원소 개수 
    for i in set(list1) & set(list2):
        a += min(dic1[i], dic2[i])
        
    # 합집합의 원소 개수
    for i in set(list1) | set(list2):
        if i in dic1 and i in dic2:
            b += max(dic1[i], dic2[i])
        elif i in dic1:
            b += dic1[i]
        else:
            b += dic2[i]

    # 자카드 유사도에 65536을 곱한 후 정수로 반환
    return int((a/b)*65536)


# 2. 다른 사람 풀이 보고: isalpha, count 사용 Code: 코드가 더 느려짐
## isalpha로 영문자 판별하기, 딕셔너리 대신에 count로 중복 개수 세기
def make_arr(s):
    l = []
    s = s.lower()
    for i in range(len(s)-1):
        if s[i:i+2].isalpha():
            l.append(s[i:i+2])
    return l

def solution(str1, str2):
    list1 = make_arr(str1)
    list2 = make_arr(str2)
    
    if not list1 and not list2:
        return 65536

    a, b = 0, 0
    # make_arr에서 set도 만들면: 조금 더 느림: 테스트 4 〉통과 (12.05ms, 10.3MB)
    for i in set(list1) & set(list2):
        a += min(list1.count(i), list2.count(i))
        
    for i in set(list1) | set(list2):
        b += max(list1.count(i), list2.count(i))

    return int((a/b)*65536)


# 3. 중복교집합, 중복합집합 구하기 Code
def make_arr(s, etc):
    arr = []
    s = s.lower()
    for i in range(len(s)-1):
        if s[i] not in etc and s[i+1] not in etc:
            arr.append(s[i:i+2])
    return arr

def solution(str1, str2):
    etc = "1234567890!@#$%^&*()-_+=[]{}<>?/\|,.;:~` "
    list1 = make_arr(str1, etc)
    list2 = make_arr(str2, etc)
    
    if not list1 and not list2:
        return 65536
    
    temp = list1[:]
    a, b = [], list1[:]
    # 직접 교집합, 합집합 구하기
    for i in list2:
        # 중복교집합 구하기
        if i in list1:
            list1.remove(i)
            a.append(i)
            
        # 중복합집합 구하기
        if i in temp:
            temp.remove(i)
        else:
            b.append(i)

    return int((len(a)/len(b))*65536)
'''
# Result
풀이 시간: 40분
1, 3 이 빠름. isalpha와 count 는 느림.
- 1. 테스트 4 〉통과 (0.76ms, 10.2MB)
- 2. 테스트 4 〉통과 (9.78ms, 10.3MB)
- 3. 테스트 4 〉통과 (0.80ms, 10.2MB)
'''


# 다른 사람 풀이: Counter 사용 -> 나중에 보고 이해하기!
## 코드 짧고, 빠름: 테스트 4 〉통과 (0.75ms, 10.2MB)
from collections import Counter

def solution(str1, str2):
    set1 = Counter([str1[i:i+2].upper() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()])
    set2 = Counter([str2[i:i+2].upper() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()])
    J = lambda A, B: 1 if len(A) == 0 and len(B) == 0 else sum((A & B).values()) / sum((A | B).values())
    return int(65536*J(set1, set2))