# 에러가 자꾸 나서 지웠다가 쓰기를 많이 반복한 것 같다
# 그냥 포기하고 답을 보려했는데 접근 방식이 똑같아서 그냥 다시 풀었다..
# 이번에는 전략을 다 짜고 들어갔는데도 이런 것을 보면 사고의 흐름에서 놓친게 있었던 것 같다

# 그리고 arr[x][i:j] = arr[x][i+1:j+1] 이런식으로 모두 풀었었는데
# 이러면 arr[i:j][y] 일 때 적용이 안된다 나는 이것도 되는줄 알았다.
# 그런데 생각해보면 연속적이지 않으니까 당연했다.
# 또 이렇게 풀면 arr[x][i:j] 가 하나만 나오는 경우가 있는데 이 때도 min을 구할 때 *을 이용하기 때문에 에러가 난다


# 이 문제는 위 오른쪽 아래 왼쪽으로 나눠서 모서리 부분은 따로 저장해두고 한칸씩 밀면 되는 문제다

def rotate(query,arr):
    x1,y1,x2,y2=map(lambda x:x-1,query)
    
    temp = [arr[x1][y2],arr[x2][y2],arr[x2][y1]]
    min_v =min(temp)

    for i in range(y2,y1,-1):
        arr[x1][i]=arr[x1][i-1]
        min_v = min(min_v,arr[x1][i])
    
    for i in range(x2,x1+1,-1):
        arr[i][y2]=arr[i-1][y2]
        min_v = min(min_v,arr[i][y2])
    arr[x1+1][y2]=temp[0]

    for i in range(y1,y2):
        arr[x2][i]=arr[x2][i+1]
        min_v = min(min_v,arr[x2][i])
    arr[x2][y2-1] = temp[1]
    
    for i in range(x1,x2-1):
        arr[i][y1]=arr[i+1][y1]
        min_v = min(min_v, arr[i][y1])
    arr[x2-1][y1]=temp[2]
    
    return [arr,min_v]
    
    
def solution(rows, columns, queries):
    answer = []
    arr = [[i for i in range(row*columns+1,row*columns+columns+1)] for row in range(rows)]
    
    for query in queries:
        arr,min_v = rotate(query,arr)
        answer.append(min_v)
        
    return answer


#처음 접근 방식은 다 나눠서 풀어야 한다는 생각을 가져서 그런지 다른 풀이를 생각 못했는데 회전시켜야할 값들을 차례로 큐에 넣고
# pop 하는 방식으로 풀면 모서리 부분을 따로 저장할 필요가 없고 최소값도 한번에 구할 수 있어서 더 간단하게 풀린다
# deque.rotate(n) 을 하면 n만큼 오른쪽으로 요소들을 밀 수 있다.. 음수면 왼쪽으로
# 파이썬은 없는게 없다..
from collections import deque

def get_nums(query,arr): # 돌려야 할 배열요소 획득
    check_arr=deque()
    x1,y1,x2,y2=map(lambda x:x-1,query)
    for i in range(y1,y2):
        check_arr.append(arr[x1][i])
    
    for i in range(x1,x2):
        check_arr.append(arr[i][y2])
        
    for i in range(y2,y1,-1):
        check_arr.append(arr[x2][i])
        
    for i in range(x2,x1,-1):
        check_arr.append(arr[i][y1])
    
    return check_arr

def rotate(query,arr,check_arr): # 요소를 돌린 후 다시 할당
    x1,y1,x2,y2=map(lambda x:x-1,query)
    check_arr.rotate(1)
    min_v = min(check_arr)
    for i in range(y1,y2):
        arr[x1][i]=check_arr.popleft()
    
    for i in range(x1,x2):
        arr[i][y2]=check_arr.popleft()
        
    for i in range(y2,y1,-1):
        arr[x2][i]=check_arr.popleft()
        
    for i in range(x2,x1,-1):
        arr[i][y1]=check_arr.popleft()
    
    return (arr, min_v)

def solution(rows, columns, queries):
    answer = []
    arr = [[i for i in range(row*columns+1,row*columns+columns+1)] for row in range(rows)]
    
    for query in queries:
        arr,min_v = rotate(query,arr,get_nums(query,arr))
        answer.append(min_v)
        
    return answer