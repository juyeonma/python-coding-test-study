'''
# 프로그래머스_[1차] 뉴스 클러스터링.py. Lv 2. 풀이: 23.06.08

# How to
- 중복도 세기 때문에, 딕셔너리로 중복의 개수를 세야한다. 
    - make_arr 함수로 집합 list 와 중복 개수를 담을 dictionary 만들기
    
- 공백이나 숫자, 특수 문자는 제거한다.
    - remove_etc 함수로 영문자 이외의 경우, False를 반환하여 집합에서 제외

- 교집합: A와 B의 딕셔너리에 있다면, 최솟값을 더해서 교집합의 길이를 구한다.
- 합집합: A와 B의 딕셔너리에 있다면, 최댓값을 더해서 합집합의 길이를 구한다.
- 최종적으로 자카드 유사도에 65536을 곱한 후 정수로 반환한다.

# Review
- re 정규식을 사용해도 되는데, 사용이 가능한지 잘 몰라서 그냥 함수로 만들었다.
    - 근데 특수문자가 저게 다인가..? 더 있는지 모르겠지만, 여튼 통과됨.
- 다른 사람 풀이를 보고 몇가지 실험해보니, 조금 느리지만, 훨씬 코드가 간단해졌다. 
    - isalpha로 영문자 판별
    - dictionary를 만들지 않음
    - a, b를 구할때 count를 사용해서 중복 원소의 개수를 구함
'''

# 1. 성공 Code
# 공백이나 숫자, 특수 문자가 있다면, False 반환
def remove_etc(s1, s2):
    etc = "1234567890!@#$%^&*()-_+=[]{}<>?/\|,.;:~` "
    if s1 in etc or s2 in etc:
        return False
    else:    
        return s1+s2

# 2개씩 끊은 문자열 list와 중복 갯수를 셀 dictionary 만들기
def make_arr(s):
    l, d = [], {}
    s = str.lower(s)
    for i in range(len(s)-1):
        tmp = remove_etc(s[i], s[i+1])
        # 영문자만 존재하는 경우,
        if tmp:
            l.append(tmp)
            if tmp in d:
                d[tmp] += 1
            else:
                d[tmp] = 1
    return l, d

def solution(str1, str2):
    list1, dic1 = make_arr(str1)
    list2, dic2 = make_arr(str2)
    
    # 집합 A와 집합 B가 모두 공집합일 경우, 유사도는 1
    if not list1 and not list2:
        return 65536
    
    a, b = 0, 0
    # 교집합의 원소 개수 
    for i in set(list1) & set(list2):
        if i in dic1 and i in dic2:
            a += min(dic1[i], dic2[i])
        elif i in dic1:
            a += dic1[i]
        else:
            a += dic2[i]
        
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


# 2. 다른 사람 풀이 보고 실험
## 조금 느려졌지만, 훨씬 간단한 코드: 테스트 4 〉통과 (9.56ms, 10.2MB)
# 변화한 부분: isalpha로 영문자 판별
def check_alpha(s1, s2):
    if s1.isalpha() and s2.isalpha():
        return s1+s2
    return False

# 변화한 부분: 딕셔너리를 만들지 않음
def make_arr(s):
    l = []
    s = s.lower()
    for i in range(len(s)-1):
        tmp = check_alpha(s[i], s[i+1])
        if tmp:
            l.append(tmp)
    return l

def solution(str1, str2):
    list1 = make_arr(str1)
    list2 = make_arr(str2)
    
    if not list1 and not list2:
        return 65536
    
    # 변화한 부분: count를 사용
    a, b = 0, 0
    for i in set(list1) & set(list2):
        a += min(list1.count(i), list2.count(i))
        
    for i in set(list1) | set(list2):
        b += max(list1.count(i), list2.count(i))

    return int((a/b)*65536)


'''
# Result
풀이 시간: 40분
테스트 4 〉 통과 (0.86ms, 10.2MB)
'''