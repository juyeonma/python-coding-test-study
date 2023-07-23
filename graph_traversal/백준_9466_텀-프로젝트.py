'''
# 백준_9466_텀-프로젝트. 골드 3. 풀이: 23.07.20 -> 실패

# How to
- DFS?

## 예시
1 -> 4
4 -> 7
7 -> 6
6 -> 4
4, 6, 7은 팀, 1은 팀이 아님.


# Review
- 풀이 시간:
- 접근방법을 모르겠다.
- dfs로 얼추 구현하려 했지만, 방법을 모르니 난잡해지고.. 틀리고..
- 원소들이 서로 연결되어 있는 것을 방문 처리로 구분했는데, 이랬더니 양방향이 아닌 다른 인덱스에서 문제가 생긴다.
- 팀에 속하는걸 방문 처리가 아닌 다른 것으로 해야할까?
'''

# Code
# 1. 실패
## 메모리:  KB, 시간:  ms
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    students = dict(zip(range(1, n+1), list(map(int, input().split()))))
    visited = {i: False for i in range(1, n+1)}
    for k in range(1, n+1):
        if not visited[k]:
            team = set()
            flag = False
            while True:
                if not flag:
                    team.add(k)
                v = students[k]
                # 연결되어 있다면,
                if v in team:
                    flag = True
                    visited[v] = True
                    team.remove(v)
                    k = v

                else:
                    # 연결이 끊겼다면,
                    if flag:
                        break
                    
                    k = v
    
    # 팀이 되지 못한 사람 수 세기
    return n - sum(visited.values())
        
for _ in range(int(input())):
    print(solve())
    
    
# 2. DFS: 실패
## 메모리:  KB, 시간:  ms
import sys
input = sys.stdin.readline

def solve():
    global answer
    n = int(input())
    students = dict(zip(range(1, n+1), list(map(int, input().split()))))
    visited = {i: False for i in range(1, n+1)}
    
    def dfs(k, team):
        global answer
        if visited[k]:
            return
        
        # 연결되어 있다면,
        if k in team:
            visited[k] = True
            return
        
        team.add(k)
        dfs(students[k], team)
        if visited[students[k]]:
            if visited[k]:
                answer += len(team)
                return
            
            visited[k] = True
            return
    
    for k in range(1, n+1):
        dfs(k, set())
    
for _ in range(int(input())):
    answer = 0
    print(solve())