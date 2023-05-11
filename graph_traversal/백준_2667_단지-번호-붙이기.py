'''
# 백준_2667_단지 번호 붙이기. 실버 1. 풀이: 23.05.09

# 풀이방법
- DFS로 풀었다.
    - 현재 집을 방문처리 후 상하좌우에 연결된 집을 방문하면서, 딕셔너리의 현재 단지에 +1을 한다.
    - DFS 반환값이 True라면, 단지 번호를 1 증가시켜 연결된 집 별로 단지를 구분한다.
- 단지의 번호를 출력한다.
- 딕셔너리의 value값이 곧 각 단지별 연결된 집의 갯수이므로, value 값을 정렬하여 출력한다.

# 보완할 것
'''

# 풀이 기록
import sys
input = sys.stdin.readline

def dfs(x, y):
    global cnt, dic

    if 0 <= x < n and 0 <= y < n and graph[x][y] == 1:
        graph[x][y] = 0
        
        if cnt in dic:
            dic[cnt] += 1
        else:
            dic[cnt] = 1
        
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    
    return False


n = int(input())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

cnt = 0
dic = {}
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            cnt += 1
        
print(cnt)
print(*sorted(dic.values()), sep='\n')

'''
# 결과
메모리: 31316 KB
시간: 40 ms
코드 길이: 629 B
'''