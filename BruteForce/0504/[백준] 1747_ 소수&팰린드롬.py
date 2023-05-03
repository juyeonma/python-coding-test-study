# 예전에 소수 판단 문제를 풀어본 적 있다. 여러개의 소수를 판단하기위한 효율적인 방법은 에라토스테네스의 체를 이용한 방법이다.
# 하지만 방법을 까먹어서 에라토스테네스의 체를 다시 읽어보고 풀었다.
# 그래도 틀렸다.
# 그 이유는 입력값이 1000000까지의 수로 제한되어있는데 출력또한 1000000까지의 수로 제한되어 있다고 생각했기 때문이었다.
# 점점 논리적인 부분이 보완되고 있다고 생각했는데 왜 자꾸 이런 틈이 생기는걸까.. 
# 1000000보다 큰 숫자중에 소수이면서 팰린드롬인 수를 구하기 위해 로컬에서 따로 코드를 짜서 1003001이 소수&팰린드롬이 되는 최대의 수라는 것을 판단하고 범위를 바꿔서 풀었다.

N=int(input())

prime_num = [1 for _ in range(1003002)]
prime_num[0:2]=[0,0]

for i in range(2,1003002):
    if prime_num[i]==0:
        continue
    for j in range(i*2,1003002,i):
        prime_num[j]=0
i=N
while True:
    if prime_num[i] and str(i)==str(i)[::-1]:
        print(i)
        break 
    i+=1


# n=1000000
# while True:
#     if str(n)==str(n)[::-1]:
#         for i in range(2,n):
#             if n%i==0:
#               break
#         else:
#             print(n)
#             break
#     n+=1