# 팰린드롬이란? 앞뒤로 읽어도 똑같은 문자
import sys
input = sys.stdin.readline
name = list(input().rstrip())
name.sort()
alphabet = {}
for i in range(len(name)):
    if name[i] in alphabet:
        alphabet[name[i]] += 1
    else:
        alphabet[name[i]] = 1

s = ""
ex = ""
for alp, i in alphabet.items():
    s += alp * (i // 2)
    # 보완할 점 : ex의 길이가 하나를 초과하면 팰린드롬이 될 수 없다.
    # if ex != '': print("~sorry~") break 하고 하나라면 바로 answer 출력했으면 더 빠르다.
    # 맨 아래 코드 참고
    if i % 2 == 1:
        ex += alp

answer = s + ex + s[::-1]
if answer == answer[::-1]:
    print(answer)
else:
    print("I'm Sorry Hansoo")


# 메모리 : 31388KB 시간 : 40ms


# 다른 사람 코드 (보완할 점을 반영한 코드)
inp = input().rstrip()
dict = {}
for alpha in inp:
    dict.setdefault(alpha, 0)
    dict[alpha] += 1

ans, center = '', ''
for alpha, cnt in sorted(dict.items()):
    if cnt%2:
        if center != '':
            print("I'm Sorry Hansoo")
            break
        center = alpha
    ans += alpha * (cnt//2)
else:
    print(ans + center + ans[::-1])