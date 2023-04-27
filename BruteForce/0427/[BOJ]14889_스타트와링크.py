import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

number = []
for i in range(n):
    number.append(i)


min_value = sys.maxsize
# 여기까지가 생각해낸 부분..
# 이후부터 감이 안잡혀서 비슷한 풀이 찾아봤다..!
# 참고 : https://heytech.tistory.com/370
s = list(combinations(number, n//2))
for start_member in s:
    start_total = link_total = 0
    # link팀원 = 전체 멤버에서 start 팀원 제외
    link_member = list(set(number) - set(start_member))

    # 팀별 능력치 계산
    for i, j in list(combinations(start_member, 2)):
        start_total += graph[i][j]
        start_total += graph[j][i]

    for i, j in list(combinations(link_member, 2)):
        link_total += graph[i][j]
        link_total += graph[j][i]

    min_value = min(min_value, abs(start_total - link_total))

print(min_value)

# dfs 풀이.. 기억해두기!
# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = list(list(map(int, input().split())) for _ in range(n))
# visited = [False for _ in range(n)]
# min_value = int(1e9)


# def dfs(depth, idx):
#     global min_value
#     if depth == n//2:
#         start = 0
#         link = 0
#         for i in range(n):
#             for j in range(n):
#                 if visited[i] and visited[j]:
#                     start += graph[i][j]
#                 elif not visited[i] and not visited[j]:
#                     link += graph[i][j]
#         min_value = min(min_value, abs(start-link))
#         return
#     for i in range(idx, n):
#         if not visited[i]:
#             visited[i] = True
#             dfs(depth+1, i+1)
#             visited[i] = False


# dfs(0, 0)
# print(min_value)

# 다시 풀어보기....

# 총평..
# 문제 잘못보고 다른 문제 풀고 있었다..(링크와 스타트 풀고 있었음..)
# 답을 넣어도 정답이 안되는 이유가 있었다..
# 다음에는 문제 잘보기..!..
