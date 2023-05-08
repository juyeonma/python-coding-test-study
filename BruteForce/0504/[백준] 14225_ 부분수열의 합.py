# 수열에 값이 있다면 새로운 배열에 추가
# 값이 없다면
# 1~ 200만1까지의 배열 만들기

# dfs로 푸는 방법이 있던데 어떻게 하는거지..

# 모든 경우의 수를 다 구해서 그 값들을 새로운 배열에 True로 반환한다.
# 새로운 배열을 차례대로 돌면서 False를 만나게 되면 해당 인덱스를 출력하고 멈춘다 

from itertools import combinations

N = int(input())
S = list(map(int,input().split()))
lis = [False for _ in range(2000001)] # 최대로 가능한 수는 N은 20까지이고 각 수는 100000 보다 작으므로 2000000이하가 된다

for v in S:
    lis[v]=True   #입력받은 수열의 인덱스를 True로 갱신

for i in range(2,len(S)+1):   # 두 개르 고르는 경우부터 전부를 고르는 경우까지 
    c = combinations(S,i)     # 각 경우마다 조합처리
    for case in c:            # 그 경우들마다 합을 구해서 그 합의 인덱스를 True로 갱신
      lis[sum(case)]=True


for i in range(1,2000001):    # 인덱스 1이 1을 뜻하므로 1부터 차례대로 확인하며 최초의 False(만들 수없는 수)를 확인하고 출력 후 break
   if not lis[i]:
      print(i)
      break