# 기존에 풀었던 풀이로는 통과가 되지 않았다
# 기존 풀이는 lock의 빈 위치를 set에 담고
# key의 돌기를 배열에 담는다
# 그리고 key와 lock응 2중 포문으로 돌면서 각각의 차이를 다 구해준 후 각 경우마다 좌표를 이동시킨다
# 그리고 key에 담은 이동한 좌표를 돌면서 lock과 일치하는지 판단하고 일차하지 않으면서 lock범위 내에 있는 좌표가 잇다면 False를 반환 그게 아니면 True를 반화시키도록 했다.
# 이것을 회전시키면서 모두 확인햇는데 틀렸다.


# 그래서 답을 보았고 배열 크기를 키워야 된다는 것을 알았다. 다음날 풀었더니 바로 풀렸다.
#lock배열을 *3만큼 가로 세로길이를 늘린다
#그 후 key를 새로운 lock에 n-m부터 2*n까지 차례로 넣으면서 합쳐진 lock을 만든다
# 그 합쳐진 lock을 for문으로 돌리면서 true인지 false인지 판단한다

#이렇게 풀 생각은 첨에 못했는데 모든 경우를 다 구해야한다는 생각에 애초에 생각을 안했다..
# 하지만 이문제는 효율성을 판단하는 문제가 아니고 키의 돌기부분이 몇 개가 있을지 모르기 떄문에 이 방법이 더 합리적이긴 한 것 같다

# 내 틀린 풀이의 경우 통과되는 코드를 만든다면 더 효율적이긴 하겠지만, 더 복잡할 것이다

# 배열 돌리기 문제가 종종 나오는 것 같다 처음엔 그냥 구현으로 돌렸는데 zip으로 하니 편하다.. 전에 이런 문제 풀 때 스터디원들 풀이에 이런 게 있었는데 그냥 넘겼었다.
# 그런데 종종 쓰이는 걸 보니 알아둬야겠다.


def rotate(arr): # 배열 90도로 돌리는 함수
    return list(zip(*arr[::-1]))

def get_new_lock(arr): # n*3의 크기의 배열로 lock을 만드는 함수, 기존의 lock은 가운데에 넣기
    new_lock=[[0]*3*len(arr) for _ in range(3*len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            new_lock[i+len(arr)][j+len(arr)]= arr[i][j]
    return new_lock

def is_match(n,attached_lock): # 새로운 lock에 key를 넣었을때 딱 들어맞는지 확인하는 함수
    for i in range(n,2*n):
        for j in range(n,2*n):
            if attached_lock[i][j]!=1:
                return False
    return True
            
def attach(key,lock,x,y): # 새로운 lock에 key를 넣는 함수
    for i in range(x,len(key)+x):
        for j in range(y,len(key)+y):
            lock[i][j]+=key[i-x][j-y]
    return lock
    
def check(n,m,key,lock):  # 가능한 가장 왼쪽위부터 오른쪽 아래까지 for문을 돌리면서 확인 
    for i in range(n-m,2*n):
        for j in range(n-m,2*n):
            new_lock=get_new_lock(lock) # lock에 key가 담기기 때문에 새로운 lock배열을 이동할때마다 만들어줘야한다 
            attached_lock=attach(key,new_lock,i,j) #lock에 key 합치기
            if is_match(n,attached_lock): # 맞는지 확인하기
                return True
    return False

def solution(key, lock):
    m,n=len(key),len(lock)
    answer = False
    if check(n,m,key,lock): # 돌리지 않았을 경우
        return True
    
    for i in range(3): # 90도씩 돌리는 경우 (90, 180 270) 확인
        key=rotate(key)
        if check(n,m,key,lock):
            return True
    return answer
# 처음 풀이는 거의 2시간 넘게 쓴 것 같고 정답 힌트를 보고 다음날에 풀었다.
# 못 풀줄 알고 시간 안재고 시도하다가 답 보려고 했는데 생각보다 빨리 풀렸다. 


# 처음 시도했던 틀린 풀이. 틀린 이유를 알고 싶지만 다시 보고 싶지 않다. 나중에 시간이 되면 봐야지
# def lotation(key):
#     new_key=[]
#     for i in range(len(key)):
#         temp=[]
#         for j in range(len(key)-1,-1,-1):
#                 temp.append(key[j][i])
#         new_key.append(temp)
#     return new_key

# def check_key_xy(key):
#     xy=[]
#     for i in range(len(key)):
#         for j in range(len(key)):
#             if key[i][j]==1:
#                 xy.append([i,j])
#     return xy

# def check_lock_xy(lock):
#     xy=[]
#     for i in range(len(lock)):
#         for j in range(len(lock)):
#             if lock[i][j]==0:
#                 xy.append((i,j))
#     return set(xy)

# def move_key_xy(key_xy,diff):
#     for i in range(len(key_xy)):
#         key_xy[i]=[key_xy[i][0]+diff[0],key_xy[i][1]+diff[1]]
#     return key_xy

# def check_result(key_xy,lock_xy,n):
#     cnt=0
#     for (x,y) in key_xy:
#         if (x,y) not in lock_xy and (0<=x<n and 0<=y<n):
#             return False
#         elif (x,y) in lock_xy:
#             cnt+=1
#     if cnt==len(lock_xy):
#         return True
#     else:
#         return False

# def diff(key_xy,lock_xy):
#     diff_xy=[]
#     for key_x,key_y in key_xy:
#         for lock_x,lock_y in lock_xy:
#             diff_xy.append([lock_x-key_x,lock_y-key_y])
#     return diff_xy

# def result(key,lock):
#     lock_xy = check_lock_xy(lock)
#     key_xy = check_key_xy(key)
#     diff_list=diff(key_xy,lock_xy)
#     for i in range(len(diff_list)):
#         new_key=move_key_xy(key_xy,diff_list[i])
#         if check_result(new_key,lock_xy,len(lock)):
#             return True
#     return False
    
    
# def solution(key, lock):
#     answer = False
#     if len(check_lock_xy(lock))==0:
#         print(1)
#         return True
#     if result(key,lock):
#         return True
#     for i in range(3):
#         key=lotation(key)
#         if result(key,lock):
#             return True     
#     return answer



