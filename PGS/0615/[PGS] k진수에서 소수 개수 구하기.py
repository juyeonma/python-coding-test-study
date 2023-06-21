# 처음 문제 봤을 때 진수 변환 문제라서 겁먹었었다
# 메서드가 있을 것 같은데 몰라서..
# 그냥 그래서 실전처럼 구현을 했고 파이썬에서는 관련 메서드가 없는 것 같다
# 근데 문제는 그게 아니었고 소수 구하는 부분이였다..

# 1번테스트 케이스가 통과가 안돼서 에라토스테네스의 체로 해보았다 
# 하지만 그렇게 하면 1번과 11번에서 런타임에러가 발생하였고 시간도 엄청 많이 걸렸다
# 그래서 진수를 바꿨을 때의 최대값을 설정하고 그만큼만 에라토스테네스의체를 돌렸는데 시간은 다 짧게 걸렸지만
# 1번과 11번은 여전히 통과가 되지 않았다.
# 그래서 힌트를 봤는데 루트를 씌워서 하면 됐었던 문제였다..
# 소수 문제를 안 푼지 오래돼서 루트를 생각 못했다...

#그런데 왜 에라토스테네스의 체로 풀면 런타임 에러가 나는걸까.. 어차피 최대값을 설정해주면 일일이 소수 구하는 거보다 더 빠를텐데 이유를 모르겠다

import math

def convert(n,k):
    arr=[]
    while n!=0:
        temp=n%k
        n//=k
        arr.append(temp)
    arr=arr[::-1]
    return "".join(list(map(str,arr)))

def check_prime(p):
    for i in range(2,int(math.sqrt(p))+1):
        if p%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    converted_n=convert(n,k)
    temp=converted_n.split("0")
    for s in temp:
        if s=="" or s=="1":
            continue
        num=int(s)
        if check_prime(num):
            answer+=1
    return answer

# 48분
#테스트1 106.80ms 10.4mb


# import math

# def convert(n,k):
#     arr=[]
#     while n!=0:
#         temp=n%k
#         n//=k
#         arr.append(temp)
#     arr=arr[::-1]
#     return "".join(list(map(str,arr)))

# def check_prime(p):
#     check = [-1]*(p+1)
#     for i in range(2,p+1):
#         if check[i]==0:
#             continue
#         check[i]=1
#         for j in range(i+i,p+1,i):
#             check[j]=0
#     return check


# def solution(n, k):
#     answer = 0
#     converted_n=convert(n,k)
#     temp=converted_n.split("0")
#     max_v=0
#     for i in temp:
#         if i=="":
#             continue
#         if max_v<int(i):
#             max_v=int(i)
#     c = check_prime(max_v)
#     for s in temp:
#         if s=="" or s=="1":
#             continue
#         num=int(s)
#         if c[num]==1:
#             answer+=1
#     return answer