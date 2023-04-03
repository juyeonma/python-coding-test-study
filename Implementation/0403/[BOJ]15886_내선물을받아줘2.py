n = int(input())
s = input()
data = [[] for i in range(len(s))]
parent = [0] * (n)

for i in range(n):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n):
    if s[i] == 'E':
        if 0 <= i + 1 < n:
            data[i+1].append(i)
            data[i].append(i+1)
    else:
        if 0 <= i - 1 < n:
            data[i-1].append(i)
            data[i].append(i-1)
for i in range(n):
    data[i] = list(set(data[i]))
for i in range(n):
    for j in data[i]:
        union_parent(parent, i, j)

print(len(set(parent)))

# 코드가 너무 길다..... => 최적화 필요!!
# EW 구간 => +1
# yevelop10	님 코드 참고!
print(s.count('EW'))
