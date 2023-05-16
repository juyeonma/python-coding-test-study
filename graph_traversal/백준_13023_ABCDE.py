'''
# 백준_13023_ABCDE. 골드 5. 풀이: 23.05.11

# How to
- A-B-C-D 연결이 되느냐? 즉 DFS를 했을때, 깊이가 4인게 존재하느냐?
- 매번 dfs를 재귀적으로 호출 할 때, 깊이를 1씩 증가킨다.
- 깊이가 4가 되면 바로 1을 출력하고 종료하고, 모든 번호에 대해서 탐색한 후에는 친구관계가 없다고 판단하고 0을 출력한다.

- 예제2
0-3-2-1-4

## 반례
5 4
0 1
0 2
2 3
3 4
Answer: 1

# Review
- 처음에는 DFS 안에 cnt와 result 변수를 넣어서 깊이를 측정했다.
    - 모든 좌표를 dfs에 넣어서 매번 가장 큰 cnt 값(=result)을 구하고, 이 값이 4보다 크면 친구관계 성공이라고 보았다.
- 그러나.. 반례를 통과해도 틀렸습니다가 떴다.
- 깊이를 어떻게 구하느냐가 문제였는데, 20분 이상 고민하다가 parameter를 증가시키는 방법을 보게 되었고, 곧 금방 성공할 수 있었다.
- 깊이 측정을 위해서 너무 많은 시간을 썼다. 왜 매개변수를 생각 못했을까?!!?
- 시간을 줄이자. 어려운 문제가 아닌데, 기본적인 문제인데도 50분이나 걸렸다..ㅠㅠ
'''

# Code
import sys
input = sys.stdin.readline

# 사람 수, 친구 관계의 수
n, m = map(int, input().split())
people = [[] for _ in range(n)]

# 친구관계에 a에 b를, b에 a를 추가
for _ in range(m):
    a, b = map(int, input().split())
    people[a].append(b)
    people[b].append(a)
    
def dfs(x, depth):
    visited[x] = True
    # 깊이가 4라면, ABCDE 관계가 성립했으므로 1 출력 후 종료.
    if depth == 4:
        print(1)
        sys.exit(0)

    for j in people[x]:
        if not visited[j]:
            dfs(j, depth+1)
            # 탐색하고 난 후에는 다시 방문 기록을 원상복구 해야함
            visited[j] = False

visited = [False] * n
for i in range(n):
    dfs(i, 0)
    # 탐색하고 난 후에는 다시 방문 기록을 원상복구 해야함
    visited[i] = False

# ABCDE 관계가 없다면, 0 출력
print(0)
    
'''
# Result
풀이 시간: 50분
메모리: 31256 KB
시간: 692 ms
코드 길이: 545 B
'''