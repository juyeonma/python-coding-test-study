'''
# 프로그래머스_67258_보석 쇼핑. Lv 3. 풀이: 23.06.18 -> 실패

# How to
- 각 보석들의 시작 index, 마지막 index, 보석별 누적 개수 기록, 최저 개수의 보석의 마지막 index 등으로 찾으려고 했으나, 실패

## 다른 사람 풀이
- 투포인터 알고리즘
    - 시작점, 끝점을 이용
    - 1. 구간이 조건에 맞을때까지 끝점을 증가시킴
    - 2. 시작점을 증가시켜 최소구간을 찾음: 매번 구간의 길이가 최소가 되도록 구간을 갱신

- 출처: 
https://velog.io/@sem/프로그래머스-LEVEL3-보석-쇼핑-Python
https://dev-note-97.tistory.com/70


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


# 다른 사람 풀이
def solution(gems):
    answer = [0, len(gems)]
    # 보석 종류는 몇개?
    size = len(set(gems)) 
    # 시작점, 끝점
    left, right = 0, 0 
    # 구간의 보석 종류: 보석 수를 담을 딕셔너리
    gem_dict = {gems[0] : 1}
    
    # 범위를 벗어나면, 종료
    while left < len(gems) and right < len(gems):
        # 현재 구간에 모든 종류의 보석이 들어있는 경우
        if len(gem_dict) == size:
            # 현재 구간의 길이가 최소라면, 구간 갱신
            if right - left < answer[1] - answer[0]: 
                answer = [left, right]
                
            # 다시 최소 구간을 찾아서 이동 -> 시작점을 증가시킴
            else:
                # 시작점을 한칸 이동시키므로, 구간에서 시작점의 보석수 -1
                gem_dict[gems[left]] -= 1
                # 만약 보석이 0개라면, 딕셔너리에서 key를 삭제 -> 삭제하지 않으면, 구간의 길이 계산시 틀리게됨
                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]  
                # 시작점 +1
                left += 1
                
        # 아직 보석을 더 찾아야 하는 경우 -> 끝점을 증가시킴
        else:
            right += 1
            
            # 범위를 벗어나면, 종료 -> while 조건에 있긴 하지만, 아래 코드로 인해 여기서 체크해야함
            if right == len(gems):
                break
            
            # 끝점이 딕셔너리에 있으면 +1, 없으면 1 추가
            gem_dict[gems[right]] = gem_dict.get(gems[right], 0) + 1
            
    # 시작 인덱스가 1번 진열대 부터 라서 1 증가
    return [answer[0]+1, answer[1]+1]


'''
# Result
풀이 시간:

'''