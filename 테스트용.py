import sys
input = sys.stdin.readline

def word(s):
    len_s = len(s)
    a = -1
    for i in range(len_s-2, -1, -1):
        if s[i] < s[i+1]:
            a = i
            break

    if a == -1:
        return False

    for j in range(len_s-1, -1, -1):
        if s[a] < s[j]:
            b = j
            break

    s[a], s[b] = s[b], s[a]
    s[a+1:] = sorted(s[a+1:])

    return s
    
for _ in range(int(input())):
    s = list(input().rstrip())
    s = word(s)
    print(''.join(s))