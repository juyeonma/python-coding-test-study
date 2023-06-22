def solution(k, tangerine):
    answer = 0
    a={} #과일 크기별 딕셔너리
    for i in tangerine: 
        if i in a: #귤의 크기가 a에 존재한다면
            a[i]+=1 #해당 크기의 귤 개수를 1 더함
        else: #존재하지 않는다면
            a[i]=1 #1을 삽입
            #---여기까지 딕셔너리 추가
    a = dict(sorted(a.items(),key=lambda x:x[1],reverse=True)) 
    # 최소한의 종류를 담기 위해서 개수가 많은 것부터 탐색하도록 함
    #딕셔너리 탐색
    for i in a:
        if k<=0: #귤을 다 골랐다면 종료
            return answer
        k-=a[i] #구하려는 귤 개수를 줄임
        answer+=1  #종류를 1 늘림
    return answer

k = int(input())
x = list(map(int, input().split()))
print(solution(k,x))