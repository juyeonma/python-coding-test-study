'''
# 프로그래머스_43163_단어 변환. Lv 3. 풀이: 23.09.05

# How to
- 변환 실패 경우: 타겟이 목록에 없거나, 타겟을 찾지 못했는데 모든 단어를 거친 경우.
- 단순하게 재귀로 들어가면서 철자를 하나씩 바꾸면서 타겟을 찾아낸다.

# Review
- 풀이 시간: 40분
- 중첩함수에서 nonlocal을 몰라서 answer을 list로 담아낼 수 밖에 없었다.
    - 전역 global, 지역 local, 비지역 nonlocal
    - 참고: https://www.daleseo.com/python-global-nonlocal/
    
# outer(), inner() 함수 입장에서 전역(global) 범위
def outer():
    # outer() 함수 입장에서 지역(local) 범위
    # inner() 함수 입장에서 비지역(nonlocal) 범위
    def inner():
        # inner 함수 입장에서 지역(local) 범위
        
- BFS로도 풀어봐야겠다.
'''

# Code
# 1. DFS: 성공
## 합계: 100.0 / 100.0
## 정확성 테스트 3 〉 통과 (0.86ms, 10.4MB)
def solution(begin, target, words):
    # target이 words 목록에 없으면, 변환 실패
    if target not in set(words):
        return 0
    
    # 변환 가능할 경우,
    # 한 단어의 길이, 단어 리스트의 길이
    n, m = len(begin), len(words)
    # 변환하면서, 중복되면 손해니까 & 무한루프 방지?
    visited = [False] * m
    answer = []

    def dfs(word, cnt):
        # 아직 타겟도 아닌데 모든 단어를 거친 경우, 변환 실패
        if cnt > m:
            return 
        
        # 타겟으로 변환한 경우, 정답에 추가
        if word == target:
            answer.append(cnt)
            return
        
        for i in range(n):
            for j in range(m):
                # 방문한 적 없고, 현재 단어의 알파벳 하나만 빼고 같은 단어일 경우,
                if not visited[j] and word[:i] == words[j][:i] and word[i+1:] ==  words[j][i+1:]:
                    visited[j] = True
                    dfs(words[j], cnt+1)
                    visited[j] = False
    
    dfs(begin, 0)
    # 타겟을 찾았다면, 즉 변환 가능 했다면 최저 cnt 반환
    if answer:
        return min(answer)
    # 타겟을 못 찾았다면, 즉 변환 불가능하다면 0 return
    else:
        return 0
