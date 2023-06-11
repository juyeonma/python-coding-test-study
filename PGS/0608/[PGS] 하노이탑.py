# 재귀의 꽃이라고 불리는 문제라는데 못풀었다..
# 아직 완벽한 재귀적인 사고가 부족한 것 같다.

# 재귀 구조
# n-1개의 원판을 출발지점에서 이웃하는 지점으로 이동시킨다.
# 마지막 원판을 출발지점에서 목적지로 이동시킨다
# 이웃하는 위치에 있는 n-1개의 원판을 목적지로 이동시킨다.

# 이제 다시 알고리즘에 애정을 갖고 공부해야겠다.. 요즘 다른거 할 게 많아서 문제 푸는 거 자체에만 집중했는데 좀 더 깊게 이해해보려고 노력해야겠다.
# 당장은 느려보여도 이게 가장 빠른길이다

# def solution(n):
#     answer = []
#     def hanoi(k,s,t):
#         if k==1:
#             answer.append([s,t])
#             return
#         hanoi(k-1,s,6-s-t)
#         answer.append([s,3])
#         hanoi(k-1,6-s-t,t)
#     hanoi(n,1,3)
#     return answer

# solution(3)


def solution(n):
    answer = []
    def hanoi(k,s,t):
        if k==0:
            return
        hanoi(k-1,s,6-s-t) #n-1개의 원판을 출발지점에서 이웃하는 지점으로 이동
        answer.append([s,t]) # 마지막 원판을 출발지점에서 목적지로 이동
        hanoi(k-1,6-s-t,t) # 이웃하는 위치에 있는 n-1개의 원판을 목적지로 이동
    hanoi(n,1,3)  # n개의 원판을 1번 기둥에서 3번 기둥으로 옮겨라
    return answer
