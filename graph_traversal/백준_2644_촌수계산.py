'''
# 백준_2644_촌수계산. 실버 2. 풀이: 23.07.06

# How to
- DFS
- 매번 b가 현재 관계들에 존재하는지 탐색한다.
    - 존재하면, 촌수를 출력하고 종료
    - 존재하지 않으면, 연결된 관계들 탐색

- bfs 안에서 b를 발견할때는 출력 후 sys.exit(0)으로 바로 종료
- bfs가 끝나고 -1 출력: b를 찾지 못했다는 뜻이므로.


# Review

'''

# 성공
import sys
input = sys.stdin.readline

def dfs(people, idx, b, depth):
    # 범위를 벗어났거나, 이미 방문했으면
    if idx > n or visited[idx]:
        return
    
    # 촌수 +1, 방문 처리
    depth += 1
    visited[idx] = True
    
    # b를 찾았으면, 촌수를 출력하고 종료
    if b in people[idx]:
        print(depth)
        sys.exit(0)
    
    # b를 찾지 못했으면, 연결된 관계를 탐색
    for i in people[idx]:
        if not visited[i]:
            dfs(people, i, b, depth)
            visited[i] = False    


n = int(input())
a, b = map(int, input().split())

people = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(int(input())):
    # 부모: 자식
    x, y = map(int, input().split())
    people[x].append(y)
    people[y].append(x) 

dfs(people, a, b, 0)
print(-1)


'''
# Result
풀이 시간: 30 분
메모리: 31256 KB
시간: 40 ms
코드 길이: 645 B
'''