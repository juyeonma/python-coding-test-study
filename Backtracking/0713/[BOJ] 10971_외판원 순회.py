import sys
input = sys.stdin.readline
n = int(input())
graph = []
data = []
answer = int(1e9)

# def solve(s):
#     global answer
#     if len(data) == n:
#         y = graph[data[-1]][data[0]]
#         if y == 0:
#             y = 1000001
#         answer = min(answer, s + y)
#         return

#     for i in range(n):
#         if i not in data:
#             data.append(i)
#             x = 0
#             if len(data) >= 2:
#                 x = graph[data[-2]][data[-1]]
#                 if x == 0:
#                     x = 1000001
#             solve(s+x)
#             data.pop()

# for _ in range(n):
#     g = list(map(int, input().split()))
#     graph.append(g)
# solve(0, 0)
# print(answer)

# 파이썬 - 시간초과 / pypy - 시간1488ms.. 

# 너무 복잡하게 생각한 것 같다.
# 다른 사람 풀이를 참고해서 수정해보기
def solve(x, s):
    global answer
    if answer < s:
        return
    if len(data) == n:
        if graph[x][data[0]]:
            answer = min(answer, s + graph[x][data[0]])
        return

    for i in range(n):
        if i not in data and graph[x][i]:
            data.append(i)
            solve(i, s+graph[x][i])
            data.pop()

for _ in range(n):
    g = list(map(int, input().split()))
    graph.append(g)
for i in range(n):
    if i not in data:
        data.append(i)
        solve(i, 0)
        data.pop()
print(answer)

# 파이썬 통과 : 메모리 - 31256	시간 - 200ms