# Counter 사용하려했는데 사용법을 까먹어서 생각하는데 시간을 좀 썼다
# 모듈 사용법이 기억에 잘 남지 않는다...ㅠㅠ
# Counter에서 키값을 모두 뽑아서 풀려고했는데 기억이 안나서 구현으로 풀었다. 그런데 풀고나서 생각해보니 values로만 풀수 있는 문제였다..

# 그리디 문제인 것 같다
# k개의 귤을 고르되 가짓수를 최소한으로 하려면 각 귤의 크기별로 가지고 있는 귤의 개수가 최대한 많아야한다. 그래야 가짓수가 최소가 되기때문
# 그러려면 귤의 개수 순으로 내림차순 정렬한 후 k에서 차례대로 빼준다 그러다가 0이 되면 딱 맞기 때문에 반환하면 되고 0이하가 되어도 해당 크기의 귤을 모두 넣을 필요가 없기때문에 그대로 반환하면 된다

# sort는 배열에서만 가능이고 sorted는 이터러블하면 모두 가능하고 배열로 변환함

# from collections import Counter
# def solution(k, tangerine):
#     answer = 0
#     counter=Counter(tangerine)
#     arr=[]
#     for i in counter:
#         arr.append([i,counter[i]])
#     arr.sort(key=lambda x:-x[1])
#     for key,value in arr:
#         if k>0:
#             k-=value
#             answer+=1
#         else:
#             break
#     return answer

# # 9분


# 최적화
# from collections import Counter
# def solution(k, tangerine):
#     answer = 0
#     counter=Counter(tangerine)
#     values = sorted(counter.values(), reverse=True)
#     for value in values:
#         if k>0:
#             k-=value
#             answer+=1
#         else:
#             break
#     return answer