import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = list(input().rstrip() for _ in range(n))
see = list(input().rstrip() for _ in range(m))

ls = list(set(listen) & set(see))
ls.sort()
print(len(ls))
for i in range(len(ls)):
    print(ls[i])

# 메모리 : 43908KB 시간 : 88ms