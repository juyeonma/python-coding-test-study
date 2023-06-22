# 유형 : 구현..?

# 실패
# 대각선을 어떻게 찾아야할까?..
# 패턴을 찾는 것에서 실패했다.
# 정사각형 방법밖에 모르겠다..
# => 질문하기 풀이법을 보았다.
# => 최대 공약수를 구하는 것이 중요한 문제였다.

from math import gcd #gcd함수를 활용해 최대 공약수를 구할 수 있다.
def solution(w, h):
    answer = 1
    if w == h:
        answer = w * h - w
    else:
        w, h = max(w, h), min(w, h)
        g = gcd(w, h)

        ww = w // g
        hh = h // g
        cut = ((ww * hh) - (ww - 1) * (hh - 1))

        answer = w * h - cut * g
    return answer

# 패턴을 어떻게 바로 찾을 수 있을까?.. 좀 더 고민해봐야겠다..

# 속도
# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10.4MB)