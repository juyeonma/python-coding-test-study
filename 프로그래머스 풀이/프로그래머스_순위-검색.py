'''
# 프로그래머스_순위 검색. Lv 2. 풀이: 23.06.14 -> 실패

# How to

# Review
- 딕셔너리를 사용하려고 했는데..생각보다 복잡하다.
    - 이중 딕셔너리를 쓴다면..?
'''

# 1. 실패 Code
def solution(info, query):
    answer = []
    n = len(info)
    info.sort()
    idx = {'cpp': [False, n], 'java': [False, n], 'python': [False, n]}

    for i in range(n):
        tmp = info[i].split()[0]
        if not idx[tmp][0]:
            idx[tmp][0] = i
            
    if idx['cpp'][0]:
        idx['cpp'][1] = min(idx['java'][0], idx['python'][0])
            
    if idx['java'][0]:
        idx['java'][1] = idx['python'][0]
        
    for q in query:
        # a, b, c, d, e
        b, c, d = True, True, True
        lang, _, job, _, career, _, food, score = q.split()

        if job == 'frontend':
            b = False
        if career == 'senior':
            c = False
        if food == 'pizza':
            d = False
            
        # 더 어떻게 구현하지..?..
        
        
    return answer
'''
# Result
풀이 시간: 실패
'''