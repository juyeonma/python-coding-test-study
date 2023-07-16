# 두 번째 방식으로 풀려다가 헤갈려서 첫번째 방식으로 풀었다. 바로 풀었는데 우왕좌왕하다보니 30분이나 걸렸다

l,c = map(int,input().split())
alpha = sorted(input().split())
moeum = {"a","e","i","o","u"}
arr=[]

def func(k,moeum_num,jaeum_num):
    if len(arr)==l and moeum_num>0 and jaeum_num>1: # 모음 1개 이상, 자음 2개 이상, 길이 l 이면
        print("".join(arr)) # 출력하기
        return
    
    for i in range(k,c): # 같은 depth에서 가능한 인덱스들
        arr.append(alpha[i]) # arr에 알파벳넣기
        if alpha[i] in moeum: # 모음이라면 모음 카운팅
            func(i+1,moeum_num+1,jaeum_num)
        else: #자음이라면 자음 카운팅
            func(i+1,moeum_num,jaeum_num+1)
        arr.pop()

func(0,0,0)

#30분
#메모리 31256kb 시간 52ms

l,c = map(int,input().split())
alpha = sorted(input().split())
moeum = {"a","e","i","o","u"}
vis = [0]*c

def func(depth,k,moeum_num,jaeum_num,result):
    if depth==l and moeum_num>0 and jaeum_num>1:
        print(result)
        return
    
    for i in range(k,c):
        vis[i]=1
        if alpha[i] in moeum:
            func(depth+1,i+1,moeum_num+1,jaeum_num,result+alpha[i])
        else:
            func(depth+1,i+1,moeum_num,jaeum_num+1,result+alpha[i])
        vis[i]=0

func(0,0,0,0,"")

#메모리 31256kb 시간 52ms