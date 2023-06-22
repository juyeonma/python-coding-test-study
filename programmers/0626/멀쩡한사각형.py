#사용할수 없는 사각형은 w+h에 최대공약수를 뺸 값이다.
import math
def solution(w,h):
    answer = 1
    answer = w*h-(w+h-math.gcd(w,h))
    return answer