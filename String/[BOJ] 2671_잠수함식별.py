import sys
input = sys.stdin.readline
s = input().rstrip()

n = len(s)

def pattern1(s):
    if s[:3] == "100" and len(s) > 3:
        s = list(s[3:])
        zero = False
        one = 0
        for i in range(len(s)):
            if s[i] == '0' and zero:
                s = s[i:]
                break
            if s[i] == '1':
                zero = True
                one += 1
        else:
            if zero:
                s = ''         
        if len(s)>2 and one > 1:
            if s[0] == '0' and s[1] == '0':
                s = '1'+ ''.join(map(str, s))
        return ''.join(map(str, s))
    return s

def pattern2(s):
    if s[:2] == "01":
        s = list(s[2:])
        for i in range(0, len(s), 2):
            if s[i] == '0' and s[i+1] == '1':
                continue
            else:
                s = s[i:]
                break
        return ''.join(map(str, s))
    return s
while s:
    temp = s
    s = pattern1(s)
    s = pattern2(s)
    if temp == s:
        print("NOISE")
        sys.exit(0)

print("SUBMARINE")

# 	메모리 : 31256	시간 : 40

# 풀었는데 너무 코드 효율이 떨어지는 것 같다.
# 보기 어렵다..