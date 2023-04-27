# 다른 방식으로 푸는 방법이 있던데 저는 잘 이해가 안가요...ㅠㅠ

from itertools import permutations
import copy
T = int(input())
arr= [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]
p = list(permutations(arr,8))

for _ in range(T):
    coins = []
    for __ in range(3):
        coins.append(list(input().split()))
    front=0
    back=0
    for i in range(3):
        for j in range(3):
            if coins[i][j]=="T":
                front+=1
            else:
                back+=1
    if front==9 or back==9:
        print(0)
        continue
    result=9
    for i in p:
        coinscopy = copy.deepcopy(coins)
        cnt=0
        f=front
        b=back
        for j in i:
            cnt+=1
            for x,y in j:
                if coinscopy[x][y]=="T":
                    coinscopy[x][y]="H"
                    f-=1
                    b+=1
                else:
                    coinscopy[x][y]="T"
                    b-=1
                    f+=1
            if f==9 or b==9:
                result=min(result,cnt)
                break
    if result==9:
        print(-1)
    else:
        print(result)