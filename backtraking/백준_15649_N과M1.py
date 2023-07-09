n,m = map(int,input().split())
s = []

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return 
    for i in range(1,n+1): #1에서부터 n까지 반복
        if i not in s: # 숫자가 중복되지 않으면
            s.append(i) #s에 추가
            # print(s)
            dfs() #조합을 구하기 위해 다시 dfs
            s.pop() #조합이 다 구해지면 pop
            # print(s)

dfs()

# 시간 : 176 ms
# 메모리 : 31256 KB
