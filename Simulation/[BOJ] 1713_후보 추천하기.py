import sys
input = sys.stdin.readline
n = int(input())
t = int(input())

student = list(map(int, input().split()))
s = {}
for i in range(t):
    if student[i] in s:
        s[student[i]][1] += 1
    else:
        if len(s) < n:
            s[student[i]] = [i, 1]
        else:
            old = sorted(s.items(), key = lambda x: (x[1][1], x[1][0]))[0]
            del(s[old[0]])

            s[student[i]] = [i, 1]

for i in sorted(s.keys()):
    print(i, end= ' ')

# 메모리 : 31256	시간 : 44

# 딕셔너리에 대한 이해가 아직 많이 부족하다는 것을 느꼈다..
# 문제 풀때마다 검색 때문에 시간이 더 오래 걸린 느낌이었다.
# 딕셔너리에 대한 공부를 많이 해야겠다