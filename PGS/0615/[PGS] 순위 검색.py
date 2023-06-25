from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def generate_combination(infos):
    info_dict=defaultdict(list)
    for info in infos:
        info=info.split()
        info_key=info[:-1]
        score=int(info[-1])
        
        for i in range(5):
            for c in combinations(info_key,i):
                tmp = "".join(c)
                info_dict[tmp].append(score)
    return info_dict

def sort_dict(info_dict):
    for key in info_dict:
        info_dict[key].sort()
    return info_dict

def solution(info, query):
    answer = []
    info_dict = generate_combination(info)
    sorted_dict = sort_dict(info_dict)
    
    for q in query:
        tmp=q.replace("and","").replace("-","").split()
        key="".join(tmp[:-1])
        score=int(tmp[-1])
        if key in sorted_dict:
            answer.append(len(sorted_dict[key])-bisect_left(sorted_dict[key],score))
        else:
            answer.append(0)
    
    return answer