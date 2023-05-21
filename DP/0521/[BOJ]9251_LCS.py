# 최대 1000글자 O(n^2)까지 가능..!

s1 = input()
s2 = input()

# ACAYKP에
# CAPCAK 순서대로 있으면 1 없으면 0 순서대로 넣었을때
#       ACAYKP
# C~ => 011001 => CAP
# A~ => 100001 => AP
# P~ => 000001 => P
# C~ => 011010 => CAK
# A~ => 100010 => AK
# K~ => 000010 => K

# 어떻게.. ACAK가 되는거지..?..

# ACAYKP
# CAPCAK

# 중간에 건너뛰는 것도 가능인가보다..?!

# 결국 답 보았다..
# 알고보니 값을 누적해주는 것이었다.
# 참고 : https://suri78.tistory.com/11
# 방법이 하나의 배열을 쓰는 법과 이중 배열을 쓰는 것이 있었는데 이중 배열이 좀 더 이해하기 쉬워서
# 일단 이중배열답을 참고했다.
# 이것도 백준에서 다시 풀기 위해 제출은 안했다..!

len1 = len(s1)
len2 = len(s2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if s1[i - 1] == s2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])