import sys
input = sys.stdin.readline
# 문자열 받기
s = list(input().rstrip())
# 1. <부터 >까지는 그대로 받기
# 2. <>가 아니라면 거꾸로 출력

# 아래 풀이는 시간이 생각보다 길다..  304-308ms정도 나옴
# data = ''
# reverse = ''
# start = []
# end = []
# for i in range(len(s)):
#     if s[i] == '<':
#         start.append(i)
#     if s[i] == '>':
#         end.append(i)
# j = 0
# if start == []:
#     start.append(int(1e9))
#     end.append(int(1e9))
# for i in range(len(s)):
#     if start[j] <= i and end[j] >= i:
#         data += s[i]
#         if end[j] == i and i != end[-1]:
#             j += 1
#     else:
#         if s[i] == ' ':
#             data += reverse[::-1]+' '
#             reverse = ''
#         else:
#             reverse += s[i]
#         if i == start[j]-1:
#             data += reverse[::-1]
#             reverse = ''
# data += reverse[::-1]
# print(''.join(data))

# 다른 사람의 풀이 : 72ms 정도 출처 : https://hongcoding.tistory.com/62
i = 0
start = 0
while i < len(s):
    if s[i] == '<':
        i += 1
        while s[i] != '>':
            i += 1
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        tmp = s[start:i]
        tmp.reverse()
        s[start:i] = tmp
    else:
        i += 1
print(''.join(s))
