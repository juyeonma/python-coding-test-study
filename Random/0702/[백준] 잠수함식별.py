# (100~1~|01)~

import re
s = input()
pattern = re.compile('(100+1+|01)+')
check = pattern.fullmatch(s)

if check:
    print("SUBMARINE")
else:
    print("NOISE")
