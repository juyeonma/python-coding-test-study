import re
s = input()
p = re.compile('(100+1+|01)+') #비교하고자하는 신호음
#정규표현식:패턴을 생성하는 방식이다...
ans = p.fullmatch(s) #s,p를 비교

if ans: 
    print("SUBMARINE")
else:
    print("NOISE")
    
# 메모리 : 34812 KB
# 시간 : 112 ms
# 코드길이 : 130 B