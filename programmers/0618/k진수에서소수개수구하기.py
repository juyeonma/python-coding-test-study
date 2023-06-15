def solution(n, k):
    answer = 0
    #정수를 진법변환
    w=""
    while n:
        w=str(n%k)+w
        n=n//k
    
    #0을 기준으로 소수를 판별해야하므로 구분
    w=w.split("0")
    #구분된 수들을 탐색
    for i in w:
        if len(i)==0 or int(i)<2: #공백이거나 0,1이면 소수가 아니므로 패스
            continue
        prime=True
        #소수 구하는 알고리즘
        for j in range(2,int(int(i)**0.5)+1):
            if int(i)%j==0:
                prime=False
                break
        if prime:
            answer+=1 #소수이면 개수 1 증가
    return answer