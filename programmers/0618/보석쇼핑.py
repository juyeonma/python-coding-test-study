def solution(gems):
    n = len(gems)
    answer = [0,n-1]
    kind = len(set(gems)) #종류 개수
    dic = {gems[0]:1} #딕셔너리에 종류 체크(첫번째는 무조건 체크)
    s,e = 0,0 #시작과 끝 위치 정의
    while s<n and e<n:
        if len(dic)<kind: #종류의 개수가 체크된 dic의 개수보다 크다면
            e+=1 #끝 위치를 한칸 뒤로 해서 범위를 넓힘
            if e==n: #옮긴 위치가 범위를 벗어나면 종료
                break
            dic[gems[e]] = dic.get(gems[e],0)+1 #현재 범위 끝에 있는 보석의 종류를 체크하는 딕셔너리에 1을 더함
        else:
            if (e-s+1)<(answer[1]-answer[0]+1): #현재 시작과 끝 위치가 최단 범위보다 작다면
                answer=[s,e] #갱신
            if dic[gems[s]]==1: # 시작위치의 종류 개수가 1이면 
                del dic[gems[s]] #시작위치의 보석을 지움
            else:
                dic[gems[s]]-=1 #1 감소,,
            s+=1 #시작위치 증가
    answer[0]+=1
    answer[1]+=1
    return answer
#다시 이해해보자,, 뭔가 모르겠다...