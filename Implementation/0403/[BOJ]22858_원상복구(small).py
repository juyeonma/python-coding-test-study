import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))


for i in range(k):
    p = [0]*n
    for j in range(n):
        p[d[j]-1] = s[j]
    s = p
print(*p)
