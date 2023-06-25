def solution(n, times):
    answer = 0
    #가장 긴 검사시간은 가장 오래걸리는 사람한테 모두 심사 받을때
    s = min(times)
    e = max(times)*n
    while s<=e:
        mid=(s+e)//2
        c = 0
        for t in times:
            c +=mid//t #mid시간동안 심사 가능한 사람 수
            if c>=n: #그것이 인원수보다 많으면 종료
                break
        if c>=n: #충분히 mid시간안에 모든 사람을 심사가능
            answer = mid
            e = mid-1
        elif c<n:
            s = mid+1
    return answer