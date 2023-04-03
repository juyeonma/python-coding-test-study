import sys
input = sys.stdin.readline
n, m = map(int, input().split())
train = [[0] * 20 for _ in range(n)]

for _ in range(m):
    comment = list(map(int, input().split()))
    if comment[0] == 1:
        train[comment[1]-1][comment[2]-1] = 1
    elif comment[0] == 2:
        train[comment[1]-1][comment[2]-1] = 0
    elif comment[0] == 3:
        train[comment[1]-1] = [0] + train[comment[1]-1][:-1]
    elif comment[0] == 4:
        train[comment[1]-1] = train[comment[1]-1][1:] + [0]

answer = []
for i in train:
    if i not in answer:
        answer.append(i)
print(len(answer))
