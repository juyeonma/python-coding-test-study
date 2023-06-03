#풀이 1
# 시간재고 푸는라 풀리는 거로 풀었는데 이 풀이는 그리디하게 풀지 못한 것 같다.
# 그리디보다는 완탐에 가깝다
# 그리고 이 문제와 비슷한 문제를 스터디할 때 풀었던 것 같은데 bfs로도 풀 수 있을 것 같다.
# 이 풀이도 어떻게 보면 bfs라고 볼 수 있긴 한 것 같다.
# 그나저나 내가 재귀로 풀다니.. 장족의 발전이다..
import sys
a,b = map(int,input().split())

def change(a,b,n):
    if a==b:
        print(n)
        sys.exit()
    if a>b: # 처음에는  sys.exit()를 했는데 그렇게 하면 여러가지경우의 수 중에 하나라도 넘어가면 종료되어서 하나의 재귀만 끝내기위해 return을 사용 
        return
    change(a*2,b,n+1) 
    temp=int(str(a)+"1")
    change(temp,b,n+1) 

change(a,b,1)
print(-1)

# 풀이시간 8분 40초
# 메모리 31256kb 시간 76ms


# 풀이 2
# 이 풀이법은 그리디한 것 같다. 
# b를 통해 a를 만들기 이런 유형을 전에 풀어봤다. 진짜 코테는 경험인가..
a,b = map(int,input().split())
cnt=1
temp=b
while a<=temp:
    if a==temp:
        print(cnt)
        break
    if temp%2==0:
        temp//=2
    else:
        if str(temp)[-1]=="1":
            temp=int(str(temp)[:-1])
        else:
            print(-1)
            break
    cnt+=1
else:
    print(-1)

#메모리 31256kb 시간 40ms
# 확실히 재귀로 했을 때보다 시간이 확 줄었다.
# 재귀는 모든 경우를 탐색하고 그리디는 최선의 방법 하나만을 탐색하기 때문이다. 