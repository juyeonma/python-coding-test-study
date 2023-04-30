# 문제 이해를 잘못해서 풀지 못했고, 풀었다고 하더라도 아래와 같은 방식으로는 못풀었을 것같은 느낌
# set을 이용한 차집합 아이디어를 기억하자
# 반대되는 팀을 어떻게 구할까 생각했었는데 차집합 아이디어가 있었다.

from itertools import combinations

N = int(input())
soccer = [list(map(int,input().split())) for _ in range(N)]

min_value = 40000
whole = list(range(N)) #0~N-1까지 범위
c = combinations(whole,N//2)  # 0~ N-1 범위안에서 절반을 뽑는 조합
for temp_start in c:    # 조합중에서 하나씩 빼서 비교하기
    start=0     # 스타트팀 능력치
    link=0      # 링크팀 능력치
    temp_link= list(set(whole)-set(temp_start)) # 전체에서 스타트팀을 제외한 절반은 링크팀
    for x,y in combinations(temp_link,2):   # 링크팀에 속한 선수들 두명씩 뽑아서 능력치 갱신
        link+=soccer[x][y]+soccer[y][x]
    for x,y in combinations(temp_start,2):  # 스타트팀에 속한 선수들 두명씩 뽑아서 능력치 갱신
        start+=soccer[x][y]+soccer[y][x]
    min_value=min(min_value,abs(start-link))  # 최소값으로 가지고있던 능력치와 현재 구한 능력치 중 최소값으로 min_value 갱신

print(min_value)