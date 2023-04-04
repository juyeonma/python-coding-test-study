import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = list(input().rstrip())
    i, j = 0, 1
    for idx in range(1, len(s)):
        print(s[idx], s[idx-1])
        if s[idx] > s[idx-1]:
            if i < idx:
                i = idx
        print(i)
    print()
    for idx in range(1, len(s)):
        print(s[idx], s[i - 1])
        if s[idx] > s[i - 1]:
            if j < idx:
                j = idx
    if i != 0 and j != 0:
        s[i-1], s[j] = s[j], s[i-1]

        s[i:] = list(reversed(s[i:]))

    print(''.join(s))

# 참고 : https://dreamtreeits.tistory.com/111
# 처음엔 순열 함수를 사용해서 풀었는데 => 시간초과
# 그 후, < 로 문자를 찾는다는 포인트만 생각해놓고 구현하지는 못했음..ㅠ..

# 참고 : https://hillier.tistory.com/102
# c++의 next_permutation 함수의 구현 방법


def nextPermutation(str):
    i = len(str)-2
    while i >= 0 and str[i] >= str[i+1]:
        i -= 1
    if i == -1:
        return False

    j = len(str)-1
    while str[i] >= str[j]:
        j -= 1

    str[i], str[j] = str[j], str[i]
    result = str[:i+1]
    result.extend(list(reversed(str[i+1:])))
    return result


answer = nextPermutation(['5', '4', '2', '1', '3'])
print(answer)
