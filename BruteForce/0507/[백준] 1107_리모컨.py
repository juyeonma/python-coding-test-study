# 현재 위치 100
# abs(현재위치-주어진 숫자)
# 해당 숫자를 바로 검색 (개수세기) 
# 해당 숫자 바로 검색할 수 없으면 그것보다 1작거나 1많은 값 가능한지 세서 > 가능한 번째+ 그 가능한 숫작개수
# 셋 중에 최소값
# import sys
# sys.setrecursionlimit(10**7)
# N = input()
# M = int(input())
# broken_btn={}
# if M:
#     broken_btn = set(input().split())

# min_click = abs(int(N)-100)

# def check_minus(n):
#     global min_click
#     for i in n:
#         if i in broken_btn:
#             check_minus(str(int(n)-1))
#             break
#     else:
#       min_click = min(min_click,(int(N)-int(n))+len(n))
#       return

# def check_plus(n):
#     global min_click
#     for i in n:
#         if i in broken_btn:
#             check_plus(str(int(n)+1))
#             break
#     else:
#       min_click = min(min_click,(int(n)-int(N))+len(n))
#       return
    
# check_minus(N)
# check_plus(N)
# print(min_click)


# 뭔가 재귀로 풀 수있을 것 같아서 재귀로 풀었지만 예외처리를 제대로 하지 못해 틀렸다.
# 그런데 재귀를 생각해보면서 재귀에 대한 이해를 조금더 할 수 있게 된것 같다.
# 문제를 똑바로 읽자고 했는데 또 똑바로 읽지 않았다... 입력값이 500000까지인것이지 누를 수 있는 것이 500000까지가아니다..
# 또한 고장난 버튼이 "있는 경우!!" 고장난 버튼이 주어진다고했는데 무조건 입력받게했다..
# 진짜 앞으로는 문제 또박또박 한글자씩 제대로 읽자! 정신차리자!

# 문제풀이 메커니즘은 비슷했던것 같다
# 하지만 최대값 설정을 어떻게 해야할지 몰랐다.

# 이렇게 최대값을 설정해서 푸는 문제에 약한 것같다.
# 요즘 왜이렇게 문제를 잘 못풀지싶다.. 자존감이 부서지고있다..
# 문제를 제대로 읽지 않아서 문제를 틀리는 경우가 크다 큰 논리는 벗어나지 않기 때문에 문제를 앞으로 똑바로 읽도록 하자

#최대값이 왜 1000000일까 일단 100번부터 500000까지 올라갈때 걸리는 횟수는 499900이다
# 그렇다면 높은수부터 내려가는 경우를 생각하면 999900까지 생각해보면 된다는 것을 알 수있다. 이 이상의 숫자에서는 어차피 abs(100-N)이 더 작다는 것을 알 수 있기 때문에
#그래서 999901까지만 판단하면 되겠지만 그냥 깔끔한 숫자로 1000000으로 한것 같다. 

N = int(input())
M = int(input())
broken_btn = {}
if M:
    broken_btn = set(input().split())

min_click=abs(100-N)

for k in range(1000000):
    num =str(k)
    for i in range(len(num)):
        if num[i] in broken_btn:
            break
    else:
        min_click=min(min_click,len(str(k))+abs(k-N))

print(min_click)
