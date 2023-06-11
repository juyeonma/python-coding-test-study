# 다음 문자열을 추가하고 그 문자열이 있으면 반복
# 다음 문자열을 추가하고 그 문자열이 없다면 마지막 문자 빼고 dict에서 찾아서 append
# 문자열을 ""으로 초기화
# while문 안에서 해결하고싶어서 문자열에 빈문자 추가
# 빈문자이기 때문에 그 문자열을 dict에 추가하고 빈문자열을 뺀 문자열을 dict에서 찾아서 append
# 빈문자열 찾을 차례에서 while문 탈출

#enumerate 기억하기

def solution(msg):
    answer = []
    idx ={v:i for (i,v) in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ",1)}
    #idx={}
    # for i,v in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ",1):
    #     idx[v]=i
    s=""
    cur=0
    msg+=" "
    while cur<len(msg):
        s+=msg[cur]
        if s==" ":
            break
        if s not in idx: # dict에 문자열이 없으면
            idx[s]=len(idx)+1 # 그 문자열 dict에 추가
            answer.append(idx[s[:-1]]) # 존재하는 부분까지 append
            s="" # 탐색하기 위해 초기화
            continue
        cur+=1
    return answer

#26분