#재귀 오류가 나서 뭔가 했더니 0을 고려 안했었다..
# 바텀업
n= int(input())
d={0:1,1:1,2:3}

def fibo(n):
    if n in d:
        return d[n]
    d[n]=fibo(n-1)+fibo(n-2)+1 # 처음에 해당 함수가 호출되므로 1을 더한다
    return d[n]

print(fibo(n)%1000000007)

# 31256kb 40ms
#풀이시간 8분


# 탑바텀
# n = int(input())
# d=[1,1,3]

# for i in range(3,n+1):
#     d.append(d[i-1]+d[i-2]+1)

# print(d[n]%1000000007)

# 31256kb 40ms