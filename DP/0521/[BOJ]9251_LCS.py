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
# 알고보니 누적
for i in range(len(s1)):
    id = i
    data = [0] * len(s1)

