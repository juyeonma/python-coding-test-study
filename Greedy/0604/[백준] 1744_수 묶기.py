# 아이디어 자체는 금방 떠올렸는데 코드를 어떻게 짜야할 지 감이 안잡혔다.
# 한번 for문 돌면서 다 구하고 싶었는데 그게 잘 안됐다.
# 지금 생각해보니까 당연했다. 음수에서는 증가하는 방향 양수에서는 감소하는 방향으로 가야 되기 때문이다
# 빠르게 풀지는 못했지만 dp 골드는 손도 못댔는데 그리디는 풀리긴 해서 기분이 묘하다 

n = int(input())
nums=[int(input()) for _ in range(n)]
result=0
minus_nums=[] 
plus_nums=[]
for i in range(n):
    if nums[i]<=0:
        minus_nums.append(nums[i]) # 0까지 음수에 담는데 음수x0은 0이기 때문에 각각 더하는 것보다 더 숫자가 커질 수 있기 때문이다.
    if nums[i]>1:
        plus_nums.append(nums[i]) # 2이상의 양수만 담는다. 1 x n 보다 1+n이 더 수가 크기 때문이다.

minus_nums.sort() # 음수 오름차순 소팅
plus_nums.sort(reverse=True) # 양수 내림차순 소팅

def s(Lst):
    global result
    for i in range(0,len(Lst),2): # 2개씩 숫자 뽑기
        if i+1<len(Lst):  # 숫자 두개씩 뽑을 수 있을때
            result+=Lst[i]*Lst[i+1]
            continue
        result+=Lst[i]  # 숫자 하나만 남을 때

s(minus_nums)
s(plus_nums)
result+=nums.count(1) # 1인경우만 구해서 더하기
print(result)


#걸린시간 1시간 8분
#메모리 31256kb 시간 40ms