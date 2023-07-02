# 유형 : 이분 탐색 =>이라고 생각하기 어려웠던 문제(근데 문제 들어가자마자 유형을 봐버렸다..)
# 유형만 알면 풀이시간은 정말 빨리 풀 수 있는데 이분탐색이라고 빨리 유형을 찾는게 중요한 것 같다.

def solution(n, times):
    start = 0
    end = times[-1] * n
    while start <= end:
        answer = 0
        mid = (start + end) // 2
        for i in times:
            answer += (mid // i)
        if answer < n:
            start = mid + 1
        else:
            end = mid - 1
        
    return start