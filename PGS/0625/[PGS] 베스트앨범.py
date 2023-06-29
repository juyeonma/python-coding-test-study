# 해시 문제를 풀면서 느낀게 복잡하게 내는 느낌이 있다.
# 좀 더 깔끔하게 풀 수는 있는데 아직 그정도 실력이 안되는 것 같다

from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dict=defaultdict(list)
    new_plays=[]
    for (i,play) in enumerate(plays): # 고유번호 저장하기 위해서
        new_plays.append((i,play))
    
    for i in range(len(genres)): # 각 장르별로 노래재생횟수 추가
        genres_dict[genres[i]].append(new_plays[i])
        
    for genre in set(genres): # 각 장르별로 분류된 dict의 노래 재생횟수들 정렬
        genres_dict[genre].sort(key=lambda x:(-x[1],x[0]))
    
    genres_sum_dict = defaultdict(int)
    for i in range(len(genres)): # 각 장르별 노래 재생횟수의 총합
        genres_sum_dict[genres[i]]+=plays[i]
    
    genres_sum_list=[]
    for k,v in genres_sum_dict.items(): #각 장르별 노래 재생횟수 총합을 리스트로 변경
        genres_sum_list.append([k,v])
    
    genres_sum_list.sort(key=lambda x:-x[1]) # 재생횟수총합 내림차순으로 장르 정렬
    
    for k,v in genres_sum_list: # 장르 내림차순으로 돌면서
        if len(genres_dict[k])>1: # 속한 노래가 2이상이면 두개 꺼내고
            answer.append(genres_dict[k][0][0])
            answer.append(genres_dict[k][1][0])
        else: # 1이면 1개만 꺼내기
            answer.append(genres_dict[k][0][0])
    return answer


# 28분