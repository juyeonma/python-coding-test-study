# input이랑 readline 속도차이가 너무 심했다

# 중복이 없고 교집합을 구하는 것이므로 set을 이용해서 구하면 된다.
ㄴ
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
no_hear = {input() for i in range(n)}
no_see = {input() for i in range(m)}

intersection = sorted(no_hear & no_see)

print(len(intersection))
print("".join(intersection))

# 메모리 44060kb 시간 84ms
# 걸린시간 : 7분

# 시간 3728ms