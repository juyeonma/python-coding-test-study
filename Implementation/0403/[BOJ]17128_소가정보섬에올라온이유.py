import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n, q = map(int, input().split())
data = list(map(int, input().split()))
q_number = list(map(int, input().split()))
s = []

for j in range(n):
    s.append(data[j] * data[(j+1) % n] * data[(j+2) % n] * data[(j+3) % n])
total = sum(s)

for i in q_number:
    total -= 2*(s[i-4] + s[i-3] + s[i-2] + s[i-1])
    s[i-4] *= -1
    s[i-3] *= -1
    s[i-2] *= -1
    s[i-1] *= -1
    print(total)

# yskang님 코드 참고하여 원래의 코드 문제 알아냄
# s[i-0] ~ s[i-4]까지는 규칙 잘 알아내었지만,
# for 문 안에서 sum(s) => 시간이 오래 걸리기 때문에 시간 초과가 일어남
# 미리 sum을 해주고 빼주기!
