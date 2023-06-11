# 너무... 막연하게 짠 것 같다..
# 효율성있게 코드를 다음에는 짜야겠다
def solution(str1, str2):
    answer = 0
    s1 = {}
    s2 = {}
    total = []
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            if str1[i : i + 2] in s1:
                s1[str1[i : i + 2]] += 1
            else:
                s1[str1[i : i + 2]] = 1
                total.append(str1[i : i + 2])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            if str2[i : i + 2] in s2:
                s2[str2[i : i + 2]] += 1
            else:
                s2[str2[i : i + 2]] = 1
                total.append(str2[i : i + 2])
    total = list(set(total))
    min_value = 0
    max_value = 0
    for i in total:
        if s1.get(i) == None:
            x = 0
        else:
            x = s1.get(i)
        if s2.get(i) == None:
            y = 0
        else:
            y = s2.get(i)
        min_value += min(x, y)
        max_value += max(x, y)
    if min_value != 0 or max_value != 0:
        answer = min_value / max_value * 65536
    else:
        answer = 65536
    return int(answer)


# 다른 사람의 풀이..
# 느낀 점 : re에 대해 처음 알았다..
# re에 대한 설명 : https://wikidocs.net/4308
# 중복을 찾아야해서 set을 사용하면 안되는 줄 알았는데 set으로 교집합 합집합을 찾고 갯수를 더해주는 방법이 있었다
import re
import math


def solution(str1, str2):
    str1 = [
        str1[i : i + 2].lower()
        for i in range(0, len(str1) - 1)
        if not re.findall("[^a-zA-Z]+", str1[i : i + 2])
    ]
    str2 = [
        str2[i : i + 2].lower()
        for i in range(0, len(str2) - 1)
        if not re.findall("[^a-zA-Z]+", str2[i : i + 2])
    ]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0:
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum / hap_sum) * 65536)


# Counter 사용하는 법
# 느낀 점 : str2[i : i + 2].isalpha() 나는 한자리씩 비교해줬는데 한꺼번에 isalpha를 사용해도 좋았다..
from collections import Counter


def solution(str1, str2):
    # make sets
    s1 = [
        str1[i : i + 2].lower()
        for i in range(len(str1) - 1)
        if str1[i : i + 2].isalpha()
    ]
    s2 = [
        str2[i : i + 2].lower()
        for i in range(len(str2) - 1)
        if str2[i : i + 2].isalpha()
    ]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(
        float(sum((c1 & c2).values())) / float(sum((c1 | c2).values())) * 65536
    )
    return answer


# 내 코드 효율적으로 짜보기
def solution(str1, str2):
    answer = 0
    s1 = []
    s2 = []
    for i in range(len(str1) - 1):
        if str1[i : i + 2].isalpha():
            s1.append(str1[i : i + 2].lower())
    for i in range(len(str2) - 1):
        if str2[i : i + 2].isalpha():
            s2.append(str2[i : i + 2].lower())
    minus = set(s1) & set(s2)
    plus = set(s1) | set(s2)

    if not s1 and not s2:
        return 65536
    else:
        min_value = 0
        max_value = 0
        for i in minus:
            min_value += min(s1.count(i), s2.count(i))
        for i in plus:
            max_value += max(s1.count(i), s2.count(i))
        answer = min_value / max_value * 65536
    return int(answer)
