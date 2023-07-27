'''
# 백준_1062_가르침. 골드 4. 풀이: 23.07.22 -> 실패

# How to
- 모든 단어는 'anta'로 시작해서 'tica'로 끝나므로, 반드시 a n t i c 의 5개 글자는 가르쳐야함.

- 배울 글자가 있다면, 두 가지 방법
    - 이번 단어는 안 읽고, 다음 단어로 넘어가기
    - 글자를 배우고 단어를 읽은 후(방문 처리), 다음 단어로 넘어가기
- 배울 글자가 없다면, 바로 이번 단어 방문처리 후 다음 단어로 넘어감 
- 그러다가 다 탐색했으면, 정답 갱신

# Review
- 풀이 시간:
- 시간초과인데, 로직에서 어느부분이 문제인지 도저히 모르겠다..
'''

# Code
# 1. 시간초과
## 메모리:  KB, 시간:  ms
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
words = [set(input().rstrip()) for _ in range(n)]

visited = [False] * n
answer = 0

def dfs(idx, alphabet):
    global answer
    
    # 모든 단어를 탐색했다면, return
    if idx == n:
        # 최댓값 갱신
        if answer < sum(visited):
            answer = sum(visited)
        return
    
    # 배울 글자가 있다면, 두 가지 방법
    if len(words[idx]) > 5:
        # 이번 단어는 안 읽고, 다음 단어로 넘어가기
        dfs(idx+1, alphabet)
        
        # 글자를 배우고 단어를 읽은 후, 다음 단어로 넘어가기
        new_alphabet = alphabet | words[idx]
        if len(new_alphabet) <= k:
            visited[idx] = True
            dfs(idx+1, new_alphabet)
            visited[idx] = False
            
    # 배울 글자가 없다면, 이번 단어를 읽고 다음 단어로 넘어감
    else:
        visited[idx] = True
        dfs(idx+1, alphabet)
    
dfs(0, {'a', 'n', 't', 'i', 'c'})

print(answer)
