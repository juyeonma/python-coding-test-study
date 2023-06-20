'''
# 프로그래머스_67258_보석 쇼핑. Lv 3. 풀이: 23.06.18 -> 실패

# How to
- 각 보석들의 시작 index, 마지막 index, 보석별 누적 개수 기록, 최저 개수의 보석의 마지막 index 등으로 찾으려고 했으나, 실패

# Review
- 뭔가 인덱스로 찾아야할거 같은데, 가닥이 잡히지 않는다.. 어떻게해야지?
'''

# Code
def solution(gems):
    n = len(gems)
    answer = [0, 0]
    arr = []
    dic = {}
    for idx, v in enumerate(gems):
        if v in dic:
            dic[v] += 1
        else:
            dic[v] = 1
        arr.append(dic[v])

    answer.append(n - arr[::-1].index(min(dic.values())))
    
    for i, v in enumerate(arr):
        if v <= dic[gems[i]]:
            answer[0] = i+1
            break
        
    # 중단 
    
    return answer

'''
# Result
풀이 시간:

'''