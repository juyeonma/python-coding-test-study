def solution(citations):
    citations.sort()
    cnt=len(citations)
    for i in range(cnt):
        if citations[i]>=cnt-i: #현재 논문인용횟수가 cnt-i보다 크다면
            return cnt-i #오름차순 정렬된 상태이므로 이대로 끝남
    return 0