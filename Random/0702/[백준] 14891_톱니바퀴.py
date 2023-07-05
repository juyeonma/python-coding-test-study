# 재귀로 하면 깔끔하게 짤 수 있을 것 같았지만 잘 다루지 못해서 그냥 하드코딩했다
# 이건 좀 아닌 것 같아서 풀고나서 재귀 풀이를 보고 다시 풀었다.

# 각 톱니를 배열에 넣고 돌아가는 지를 확인하고 deque.rotate를 이용해서 돌려주면 편하게 구할 수있다.

# from collections import deque

# gear= []
# for _ in range(4):
#     gear.append(deque(input()))

# k = int(input())
# for _ in range(k):
#     num,direction = map(int,input().split())
#     dir_temp = [0,0,0,0]
#     if num==1:
#         dir_temp[0]=direction
#         if gear[0][2]!=gear[1][6]:
#             dir_temp[1]=direction*(-1)
#             if gear[1][2] != gear[2][6]:
#                 dir_temp[2]=dir_temp[1]*(-1)
#                 if gear[2][2]!=gear[3][6]:
#                     dir_temp[3]=dir_temp[2]*(-1)
#     elif num==2:
#         dir_temp[1]=direction
#         if gear[1][2]!=gear[2][6]:
#             dir_temp[2]=direction*(-1)
#             if gear[2][2]!=gear[3][6]:
#                 dir_temp[3]=dir_temp[2]*(-1)
        
#         if gear[0][2]!=gear[1][6]:
#             dir_temp[0]=direction*(-1)

#     elif num==3:
#         dir_temp[2]=direction
#         if gear[2][2]!=gear[3][6]:
#             dir_temp[3]=direction*(-1)
        
#         if gear[1][2]!=gear[2][6]:
#             dir_temp[1]=direction*(-1)
#             if gear[0][2]!=gear[1][6]:
#                 dir_temp[0]=dir_temp[1]*(-1)

#     else:
#         dir_temp[3]=direction
#         if gear[2][2]!=gear[3][6]:
#             dir_temp[2]=direction*(-1)
#             if gear[1][2]!=gear[2][6]:
#                 dir_temp[1]=dir_temp[2]*(-1)
#                 if gear[0][2]!=gear[1][6]:
#                     dir_temp[0]=dir_temp[1]*(-1)

#     for i in range(len(dir_temp)):
#         gear[i].rotate(dir_temp[i])

# answer=0
# for i in range(len(gear)):
#     if gear[i][0]=="1":
#         answer+=2**(i)

# print(answer)

# 34364kb 72ms
# 40분

from collections import deque

gear= []
for _ in range(4):
    gear.append(deque(input()))

k = int(input())

def check_right(x,d):

    if x>3 or gear[x-1][2]==gear[x][6]:
        return
    
    if gear[x-1][2]!=gear[x][6]:
        check_right(x+1,-d)
        gear[x].rotate(d)

def check_left(x,d):
    if x<0 or gear[x][2] == gear[x+1][6]:
        return

    if gear[x][2]!=gear[x+1][6]:
        check_left(x-1,-d)
        gear[x].rotate(d) 
    

for _ in range(k):
    num,direction = map(int,input().split())

    check_right(num,-direction)
    check_left(num-2,-direction)
    gear[num-1].rotate(direction)


answer=0
for i in range(len(gear)):
    answer+=(2**(i)) * int(gear[i][0])

print(answer)

# 34308kb 68ms