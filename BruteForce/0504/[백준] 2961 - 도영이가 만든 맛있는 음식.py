# 넉넉하게 잡아도 시간복잡도는  O(n^2)  100만이 넘지 않는다 > 완전탐색
# 쓴맛을 1~ N개 까지 선택하는 조합 구해서 각 경우 다 곱하기
# 단맛을 1~N개 까지 선택하는 조합 구해서 각 경우 다 더하기

# 자꾸 틀려서 이유가 뭘까 생각해봤는데 재료를 각각 사용하는것으로 착각했다.
# 4
# 1 7
# 2 6
# 3 8
# 4 9 면 1, 2, 3, 4, 1 2, 1 3,...      7, 6, 8, 9, 7 6, 7 8, 모두 각각의 경우의수를 다 구해야하는 줄 알았다.
# 하지만 그게 아니었고 재료를 사용할 때 한 줄은 한번에 사용하는 것이었다.

# 조합을 이용해서 구하면 되는 문제
from itertools import combinations

N = int(input())
taste = [list(map(int,input().split())) for _ in range(N)]
bitter=[] 
sweet=[]
for a,b in taste:   #쓴맛과 단맛에 요소 나누어 담기
    bitter.append(a)
    sweet.append(b)

min_taste=1000000000       #임의의 최대값

for i in range(len(bitter)):   # 하나씩만 선택해서 최소값구하는경우
    min_taste=min(min_taste,abs(bitter[i]-sweet[i]))  

bitter_sum=[]
sweet_sum=[]
for i in range(2,N+1):      # 두 개 이상 선택해서 최소값 구하는 경우
    b_comb = combinations(bitter,i)
    s_comb = combinations(sweet,i)

    for case in b_comb:     # 쓴맛에 대한 조합 경우의수 전부 구하기
        temp_b_sum=1
        for j in case:
            temp_b_sum*=j
        bitter_sum.append(temp_b_sum)
    
    for case in s_comb:     # 단맛에 대한 조합 경우의 수 전부 구하기
        temp_s_sum=0
        for j in case:
            temp_s_sum+=j
        sweet_sum.append(temp_s_sum)

for i in range(len(bitter_sum)):    # 순차적으로 돌면서 최소값 구하기
    min_taste=min(min_taste,abs(bitter_sum[i]-sweet_sum[i])) 

print(min_taste)
