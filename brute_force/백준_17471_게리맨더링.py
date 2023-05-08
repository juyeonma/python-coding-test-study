'''
# 백준_17471_게리맨더링. 골드 4. 풀이: 23.05.05
# 풀이방법
- 빠진 구역이 없어야 하고, 서로 연결되어 있어야하며, 인구수 차이가 적어야함.
- 모든 조합에 대하여 bfs로 탐색하자.
- bfs에서 인구 수와 구역 수를 반환 -> 구역 수 더했을때 전체 구역수가 나온다면, 인구 수 차이 최솟값 갱신.
'''

'''
# 보완할 것
- 전형적인 bfs 문제여서 쉬웠다.
- 다만, 빠진 구역이 없는지 체크하는것을 소홀히 하지 않는게 포인트?
'''

# 풀이 기록
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# 구역의 개수
n = int(input())

# 1~n 구역의 인구. 0번은 없으므로 0으로 놔둠.
people = [0] + list(map(int, input().split()))

city = [[] for _ in range(n+1)]

for i in range(1, n+1):
    a, *b = map(int, input().split())
    for j in b:
        city[i].append(j)
        city[j].append(i)

visited = [False] * (n+1)

# bfs 함수
def bfs(combi):
    start = combi[0]
    cnt = 0
    q = deque([start])
    visit = visited[:]
    visit[start] = True
    
    while q:
        v = q.popleft()
        cnt += people[v]
        for i in city[v]:
            if i in combi and not visit[i]:
                q.append(i)
                visit[i] = True
    
    # 인구 수, 조건을 통과한 구역 수
    return cnt, sum(visit)

answer = int(1e9)
for i in range(1, n//2+1):
    combis = list(combinations(range(1, n+1), i))
    for j in combis:
        # 인구 수, 구역 수
        a1, b1 = bfs(j)
        a2, b2 = bfs([i for i in range(1, n+1) if i not in j])
        # bfs에서 조건을 통과한 구역 수를 더했을때 전체 구역수가 나오는지
        # 즉, 빠진 구역은 없는지 체크
        if b1 + b2 == n:
            answer = min(answer, abs(a1-a2))

if answer != int(1e9):
    print(answer)
else:
    print(-1)
'''
# 결과
메모리: 34192 KB
시간: 72 ms
코드 길이: 1119 B
'''