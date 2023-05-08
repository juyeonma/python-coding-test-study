#[백준] 3085 - 사탕 게임 
n = int(input())
gragh=[list(input()) for _ in range(n)]
cnt=0

def check():
  global cnt
  for i in range(n):
    c=1
    for j in range(1,n):
      if gragh[i][j]==gragh[i][j-1]:
        c+=1
        cnt=max(c,cnt)
      else:
        c=1
    c=1
    for j in range(1,n):
      if gragh[j][i]==gragh[j-1][i]:
        c+=1
        cnt=max(c,cnt)
      else:
        c=1
for i in range(n):
  for j in range(n):
    if j+1<n:
      gragh[i][j], gragh[i][j+1]=gragh[i][j+1], gragh[i][j]
      check()
      gragh[i][j], gragh[i][j+1]=gragh[i][j+1], gragh[i][j]
    if i+1<n:
      gragh[i][j], gragh[i+1][j]=gragh[i+1][j], gragh[i][j]
      check()
      gragh[i][j], gragh[i+1][j]=gragh[i+1][j], gragh[i][j]

print(cnt)