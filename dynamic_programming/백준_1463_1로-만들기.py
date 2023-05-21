'''
# 백준_1463_1로 만들기. 실버 3. 풀이: 23.05.16 -> 실패

# How to
- 1, 2, 3의 연산 횟수: 0, 1, 1
- 방식: 
    - 1) Top-Down
    - 2) Bottom-Up
    
- 로직: 
    - 1) 2와 3 나머지 경우의 수에 따라 최솟값 구하기: if n%3==0 and n%2==0 ~ elif~ elif~ else
    - 2) 2와 3의 몫과 나머지 덧셈 이용한 최솟값 구하기: (n//3)의 값+(n%3), (n//2)+(n%2) 중 최솟값 + 1
    - n-1을 추가하면? Top-Down: 시간초과, Bottom-Up: 시간 약간만 증가
                
- 횟수 저장: 
    - 1) list: Bottom-Up에서 좋음
        - Top-Down에서는 RecursionError 발생
            - sys.setrecursionlimit(10**6) 추가해도, 메모리 초과
    - 2) dictionary: Top-Down 에서 좋음
        - Bottom-Up에서는 메모리와 시간 증가. 그리고 탐색범위 신경써야함.
    
- 바텀업에서 탐색범위: 
    - 1) dictionary 저장: 로직에 따라 4부터 탐색해야할 수도 있음
    - 2) list 저장: 2부터 탐색. 만약 4부터 탐색하려면? n의 크기대로 2와 3 저장
    
## 예제
10
- 1을 빼고(=9) 3으로 나누고(=3) 3으로 나누면(=1) : 3번
- 2로 나누고(=5) 1을 빼고(=4) 2로 나누고(=2) 2로 나누면(=1): 4번
-> 당장은 2로 나눠야 더 작은 수지만, 오히려 1을 뺀 후 3으로 나누는게 더 빨리 줄어든다


# Review
- 결국 실패해서 구글링을 하였고, 엄청 많은 시간을 소모했지만, DP 공부가 제대로 됐다.
- 여러번 실험을 하고, 몇가지를 깨달았다.
    - 비슷한 로직으로 보여도 시간과 메모리가 차이나거나, 에러나 초과가 뜰 수 있다.
    - index를 고려하자. 
        - dictionary라면 key가 존재하지 않을 경우를, list라면 n의 크기를 고려하자.
    - dictionary와 list 중 적절히 선택하자. 
        - Top-Down에서 list는 메모리 초과가 발생했고, Bottom-Up에서 dictionary는 매우 큰 메모리와 시간을 소모했다.

- 결과적으로 가장 효율적인 코드: 2번
    - Top-Down, 몫과 나머지 덧셈으로 최솟값 구하기, dictionary 저장
    - 이때, 최솟값 구할 때 n-1은 넣지 않는다.        
'''


# 1. Top-Down Code
## 1번: 31256 KB, 44 ms
n = int(input())
check = {1: 0, 2: 1, 3: 1} # 횟수 저장: 2) dictionary

# 로직: 1) 2와 3 나머지 경우의 수에 따라 최솟값 구하기
def make_one(n):
    if n in check:
        return check[n]

    if n%3==0 and n%2==0:
        '''
        만약 min에 make_one(n-1) 추가하면, RecursionError
        sys.setrecursionlimit(10**6) 추가해도, 시간초과
        '''
        check[n] = min(make_one(n//3), make_one(n//2)) + 1
    
    elif n%3==0:
        check[n] = min(make_one(n-1), make_one(n//3)) + 1
        
    elif n%2==0:
        check[n] = min(make_one(n-1), make_one(n//2)) + 1
        
    else:
        check[n] = make_one(n-1) + 1
        
    return check[n]

print(make_one(n))


## 2번: 31256 KB, 40 ms
n = int(input())
check = {1: 0, 2: 1, 3: 1} # 횟수 저장: 2) dictionary

# 로직: 2) 2와 3의 몫과 나머지 덧셈 이용한 최솟값 구하기
def make_one(n):
    if n in check:
        return check[n]
    '''
    만약 min에 make_one(n-1) 추가하면, RecursionError
    sys.setrecursionlimit(10**6) 추가해도, 시간초과
    '''
    check[n] = min(make_one(n//3)+(n%3), make_one(n//2)+(n%2)) + 1    
    return check[n]
    
print(make_one(n))


# 2. Bottom-Up Code
## 3번: 39068 KB, 464 ms
n = int(input())
'''
만약 4부터 탐색하려면? n의 크기에 따라 2와 3의 거리 저장
if n > 2: check[2], check[3] = 1, 1
elif n > 1: check[2] = 1
만약 dictionary에 저장하면? 메모리와 시간이 증가: 115228 KB, 636 ms
'''
check = [0] * (n+1) # 횟수 저장: 1) list -> for문의 탐색 범위를 2부터 시작

# 로직: 1) 2와 3 나머지 경우의 수에 따라 최솟값 구하기
for i in range(2, n+1):
    if i%3==0 and i%2==0:
        '''
        만약 min에 check[i-1]을 추가하면, 시간 약간 증가
        '''
        check[i] = min(check[i//3], check[i//2]) + 1
    
    elif i%3==0:
        check[i] = min(check[i-1], check[i//3]) + 1
        
    elif i%2==0:
        check[i] = min(check[i-1], check[i//2]) + 1
        
    else:
        check[i] = check[i-1] + 1
        
print(check[n])


## 4번: 39068 KB, 536 ms
n = int(input())
'''
list 저장: 2부터 탐색 -> 만약 4부터 탐색? n의 크기에 따라 2와 3저장: 시간은 비슷
만약 dictionary 저장: 4부터 탐색: 115228 KB, 668 ms-> 만약 2부터 탐색? KeyError: key에 0이 없어서
'''
check = [0] * (n+1) # 횟수 저장: 1) list

# 로직: 2) 2와 3의 몫과 나머지 덧셈 이용한 최솟값 구하기
for i in range(2, n+1):
    '''
    만약 min에 check[i-1]을 추가하면 메모리는 그대로, 시간은 약 100 ms 정도 증가
    '''    
    check[i] = min(check[i//3]+(i%3), check[i//2]+(i%2))+1
print(check[n])


'''
# Result
풀이 시간: 실패했으므로, X
## 2번 풀이
메모리: 31256 KB
시간: 40 ms
코드 길이: 452 B
'''