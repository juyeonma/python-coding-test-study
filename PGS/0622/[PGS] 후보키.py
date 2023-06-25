# 막구현해보려다가 30분날리고 다시 전략짜고 들어가서 풀었다 그래도 오래 걸렸네..
# 카카오문제는 너무 복잡하고 어려운 것 같다..ㅠㅠ
# 메서드를 많이 알고있으면 좋은 것 같은데 어떻게 다 외우지..
# 나올때마다 기억하려고 노력해야겠다.
from itertools import combinations

def index_combination(n): # 속성을 왼쪽부터 0 ~ n-1까지 두고 모든 가능한 집합을 배열에 넣기
    arr=[]
    for i in range(n):
        for c in combinations(range(n),i+1):
            arr.append(list(c))
    return arr

def tuple_combination(tup): # 각 튜플 별로 조합 경우의 수 구하기
    arr=[]
    for i in range(1,len(tup)+1):
        for c in combinations(tup,i):
            arr.append("".join(c))
    return arr

def solution(relation):
    answer=[]
    relations=[] # 모든 튜플들을 다 넣고 각 요소에는 튜플의 조합이 담긴다
    for tup in relation:
        relations.append(tuple_combination(tup))
    
    attribute_index= index_combination(len(relation[0]))
    
    for i in range(len(relations[0])):
        temp=[]
        for j in range(len(relations)):
            temp.append(relations[j][i]) # 같은 속성인 경우를 찾아서 temp에 넣기
        
        if len(temp)==len(set(temp)): # 유일성 판단
            for j in answer: # for문 돌면서 최소성 판단
                if set(j)&set(attribute_index[i])==set(j):
                    break
            else:
                answer.append(attribute_index[i])
    return len(answer)


#걸린시간: 1시간 12분



# 비슷한 풀이인데 유일성 최소성판단하기 전에 튜플을뽑는과정이 좀 다르다
# 나는 뽑아서 문자열로 판단했지만 여기서는 튜플을 set으로 바꿔서 메서드를 사용한다.
from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
        
    #유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        if len(set(tmp)) == row:    # 유일성
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break
                    
            if put: unique.append(i)
   
    return len(unique)