# 각 위치를 딕셔너리에 담고 왼손접근가능한 곳과 오른손 접근 가능한 곳을 나눠서 좌표를 이동하며 구한다

left,right = input().split()
s = input()
keys_dict = {}
keys = ["qwertyuiop","asdfghjkl","zxcvbnm"]
for i in range(len(keys)):
    for j in range(len(keys[i])):
        keys_dict[keys[i][j]]=(i,j)

cons=set(["q","w","e","r","t","a","s","d","f","g","z","x","c","v"])

x1,y1 = keys_dict[left]
x2,y2 = keys_dict[right]

cnt=0
for v in s:
    next_x,next_y=keys_dict[v]
    if v in cons:  
        cnt+=abs(next_x-x1)+abs(next_y-y1)+1
        x1,y1= next_x,next_y
    else:
        cnt+=abs(next_x-x2)+abs(next_y-y2)+1
        x2,y2= next_x,next_y

print(cnt)

#메모리 31256kb 시간 40ms
#걸린시간 10분?
