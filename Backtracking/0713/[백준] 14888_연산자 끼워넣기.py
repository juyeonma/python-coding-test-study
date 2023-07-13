# 백트래킹을 풀면서 for을 이용해서 푸는 문제만 풀어서 그런지 이 문제도 for문으로 접근 하려다가 못풀었다.
# 깊이가 깊어지면서 확인하는 것이 백트래킹. 본질을 잊지말자
# 백트래킹 이해는 어느정도 한 것 같고 이제 많이 풀어보면서 깊이 이해하며 익숙해져야겠다
#순열로 풀었으면 더 쉽게 풀었을 것 같긴하다

n = int(input())
nums = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())
max_value = -1000000000
min_value = 1000000000

def func(depth,result):
    global add,sub,mul,div,max_value,min_value

    if depth == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    else:
        if add>0:
            add-=1
            func(depth+1,result+nums[depth])
            add+=1
        if sub>0:
            sub-=1
            func(depth+1,result-nums[depth])
            sub+=1
        if mul>0:
            mul-=1
            func(depth+1,result*nums[depth])
            mul+=1
        if div>0:
            div-=1
            func(depth+1,int(result/nums[depth]))
            div+=1

func(1,nums[0])
print(max_value,min_value,sep="\n")