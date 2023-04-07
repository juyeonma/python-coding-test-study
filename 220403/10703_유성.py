r,s = map(int, input().split())
gragh=[]
for i in range(r):
    gragh.append(input())
    
arr=[['.']*s for _ in range(r)]

max_meteor = [-3333] *s
min_ground=[1<<14]*s

for i in range(r):
    for j in range(s):
        if gragh[i][j]=='X':
            max_meteor[j]=max(max_meteor[j],i)
        elif gragh[i][j]=='#':
            min_ground[j] = min(min_ground[j], i)
            
move = min((j-i for i,j in zip(max_meteor,min_ground)))-1

for i in range(r):
    for j in range(s):
        if gragh[i][j]=='X':
            arr[i+move][j]='X'
        if gragh[i][j]=='#':
            arr[i][j]='#'
            
for i in range(r):
    for j in range(s):
        print(arr[i][j], end='')
    print()