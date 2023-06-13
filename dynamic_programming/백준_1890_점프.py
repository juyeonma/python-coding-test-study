n = int(input())
array=[]
for i in range(n):
  array.append(list(map(int, input().split())))

dp = [[0]*(n) for _ in range(n)] #dp리스트 초기화
dp[0][0]=1 #시작은 한번 방문된것이니까 1

for i in range(n):
  for j in range(n):
    if i==n-1 and j ==n-1: #현재 위치가 오른쪽 끝이라면 그때의 dp값 출력
      print(dp[i][j])
      break
    if j + array[i][j] <n: #j의 값이 증가됐을 때, n보다 작으면
      dp[i][j+array[i][j]] += dp[i][j] #점프했을 때 위치에 현재의 값과 점프 위치에서의 값을 더함
    if i + array[i][j]<n:
      dp[i+array[i][j]][j] += dp[i][j]


# 코드길이 : 630 B
# 시간 : 40 ms
# 메모리 : 31256 KB