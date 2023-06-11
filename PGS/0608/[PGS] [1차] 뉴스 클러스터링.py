# 이전에 풀어본 문제인데 또 오래걸렸다.. 그런데 전과는 다른 방식으로 풀었다.
# 이번에도 좀 복잡하게 푼 것 같은데 이전에 풀었떤 풀이는 좀 더 복잡하게 풀었었다.
# isalpha 이런거 다 외워둬야되나... 이것만 찾아서 풀었다.

# 집합을 사용해서 풀고 싶었는데 set을 적용할 수 없다고 판단해서 사용하지 못했다
# 하지만 정답인 풀이에 set을 사용한 풀이가 있는데 벽느껴졌다..물론 그 풀이는 시간복잡도가 좀 더 나올 수 있겠지만 통과만 되면 되기 때문에 그 풀이가 더 깔끔한 것 같다.

# 또 Counter를 사용하면 더 짧게 집합으로 풀 수 있다


#먼저 문자열들을 소문자로 변환한 뒤, 영어로 된 두글자문자열을 하나의 변수에 모두 담는다.
#동시에 dict를 사용하여 두글자 문자열을 모두 센다
# 가능한 문자열에 담은 배열을 돌면서 두 dict에 모두 들어있으면 더 개수가 많은건 합집합에, 적은건 교집합에 넣는다.
# 한쪽만 존재하는 문자열이라면 합집합에만 넣는다.

def solution(str1, str2):
    str1=str1.lower() # 소문자로 변환
    str2=str2.lower()
    possible_str = set() # str1,str2에서 가능한 문자열을 모두 담는 변수
    str1_dict = {} # str1에서 가능한 문자열 세기
    str2_dict = {} 
    intersection=0 # 교집합 원소 개수
    union=0  # 합집합 원소 개수
    for i in range(len(str1)-1): #두글자씩 나눠서 영문자로만 된 문자열을 넣고, str1_dict에도 넣으면서 세기
        if not str1[i:i+2].isalpha():
            continue
        possible_str.add(str1[i:i+2])
        if str1[i:i+2] not in str1_dict:
            str1_dict[str1[i:i+2]]=0
        str1_dict[str1[i:i+2]]+=1
        
    for i in range((len(str2)-1)):
        if not str2[i:i+2].isalpha():
            continue
        possible_str.add(str2[i:i+2])
        if str2[i:i+2] not in str2_dict:
            str2_dict[str2[i:i+2]]=0
        str2_dict[str2[i:i+2]]+=1
    
    possible_str = list(possible_str)
    
    for s in possible_str:  # 문자열을 돌리면서
        if s in str1_dict and s in str2_dict: # 둘다있으면 많은것은 합집합 적은건 교집합
            if str1_dict[s]<=str2_dict[s]: 
                union+=str2_dict[s]
                intersection+=str1_dict[s]
            else: 
                union+=str1_dict[s]
                intersection+=str2_dict[s]
        elif s in str1_dict: #한쪽만 있는 경우는 합집합에만 더하기
            union+=str1_dict[s]
        else:
            union+=str2_dict[s]
    
    if union==0: # 합집합이 0이면 교집합도 0이므로 합집합이 0이라면 65536 담기
        answer=65536
    else: #정답 담기
        answer = (intersection/union)*65536//1
    return answer

#걸린시간 42분



# dict에는 집합연산이 안되지만 Counter는 된다..
from collections import Counter

def solution(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = Counter([str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]) # 영문자로만 된 문자열 담기
    s2 = Counter([str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()])
    
    answer = 65536 if len(s1)==0 or len(s2)==0 else (sum((s1&s2).values())/sum((s1|s2).values()))*65536//1 
    # 공집합이면 65536 담고 그게 아니라면 연산한 것 담기
    return answer


# 이렇게도 가능하다
# 위에서 말햇듯이 이렇게하면 intersection_sum에서 2중 for문이 되어 효율적이지 못하긴 하다
# 하지만 n이 1000이하로 작기 때문에 문제가 없다
# 효율을 생각하다보니 이런 풀이를 머릿속에서 계속 떠올리지 못하게 된다
# 노력해야겠지
def solution(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()] 
    s2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    intersection = set(s1) & set(s2)
    union = set(s1) | set(s2)
    if len(union)==0:
        return 65536
    intersection_sum = sum([min(s1.count(gyo), s2.count(gyo)) for gyo in intersection]) # 교집합을 돌리면서 s1,s2 중 적은것 선택
    union_sum = sum([max(s1.count(hap), s2.count(hap)) for hap in union]) #합집합 돌리면서 s1,s2 중 많은 것 선택
    return (intersection_sum/union_sum)*65536//1

# 집합으로 제거하고 카운트로 세는 부분이 정말 경악을 금치 못했다...