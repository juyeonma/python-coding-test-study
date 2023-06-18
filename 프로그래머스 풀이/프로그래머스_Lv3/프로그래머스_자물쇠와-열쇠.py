'''
# 프로그래머스_자물쇠와 열쇠. Lv 3. 풀이: 23.06.11

# How to
- 성공 조건: key와 lock을 더했을 때 lock의 모든 원소가 1이 되게 만들자
- key를 회전할 수 있으므로, 90도씩 회전한 list를 만듦:
    원본,
    시계 방향 90도
    시계 방향 180도
    시계 방향 270도(=반시계 방향 90도):
    
    1 2 3   7 4 1   9 8 7   3 6 9
    4 5 6   8 5 2   6 5 4   2 5 8
    7 8 9   9 6 3   3 2 1   1 4 
    
- key는 lock보다 작으므로, lock을 3배 확장시켜서 상하좌우에 하나씩 붙임(=big_lock)
- 복사한 big_lock에서 좌표를 이동하며 key와 더함
- 원래 lock의 배열이 모두 1이라면, 즉 set했을때 1만 남았다면, 성공


# Review
- 여러번 푼 문제인데도, 한번 풀때마다 오래 걸린다.
    - 배열을 90도씩 돌리는 코드를 짜는데 오래 걸리고,
    - lock과 key를 맞춰볼 때 index 범위를 설정하는데 잦은 실수를 한다.
    
- 그럼에도 불구하고, 예전에 풀 때와 오늘 풀 때 차이가 발생했다.
    - key를 회전시킬 때 코드가 조금 단축되었다. 예전에는 무조건 list안에 list로 했는데, 이번에는 tuple로 놔두었다.
        - 어짜피 lock을 복사할 테고, 인덱싱만 가능하다면, 굳이 list로 만들 필요가 없어 보인다.
    - 이번엔 key와 lock을 맞춰보는걸 별도의 함수로 만들었다.
    - lock과 key를 더하거나 lock이 모두 1이 되었는지 확인할 때,
        - 예전에는 set, sum, map, lambda 등을 사용해서 한줄로 구했다면, 
        - 이번에는 for문으로 좌표 혹은 한 행씩 더하거나 set을 사용했다. 
- 결과적으로 이번 코드는 무작정 for문을 여러개 써서 일일히 구현했기에 조금 더 이해가 쉽고 빨랐다면,
    예전 코드는 한줄 부분이 짧지만 나름 복잡해서 단번이 이해되지는 않았다.
    그래도 예전 코드가 나름 마음에 들었기에.. 어떻게 더 효율적으로 줄일 수는 없을까?
    
- 그런데 자꾸 key를 돌리게 된다.. 다른 방법으로 풀 수는 없을까?
'''

# 1. 오늘 Code: 성공
## 테스트 11 〉	통과 (322.78ms, 10.3MB)
def unlock(m, key, n, lock_end, big_start, big_end, big_lock):
    # 상하좌우로 확장한 lock을 살펴봄
    for i in range(big_start, big_end):
        for j in range(big_start, big_end):
            # 매번 더하기 위해서, 복사해둠
            big_lock_copy = [i[:] for i in big_lock]
            # key의 좌표를 살펴서
            for x in range(m):               
                for y in range(m):
                    # lock에 key를 더함
                    big_lock_copy[i+x][j+y] += key[x][y]

            # 원래 lock이 모두 1이 되었다면, 성공
            for ii in range(n, lock_end):
                # lock에 남은 홈이 있거나, 돌기+돌기라면, 실패 -> 다음 좌표로 이동
                if set(big_lock_copy[ii][n:lock_end]) != {1}:
                    break
            else:  
                return True
            
    # 이번 key에서는 lock과 맞는 부분을 찾지 못함
    return False

def solution(key, lock):
    # 원본, 시계 방향 90도, 180도, 270도 회전
    ## 시계 방향 180도: list(map(list, map(reversed, reversed(key)))) 도 가능
    keys = [key,
            list(zip(*reversed(key))), # list 안에 tuple
            [list(i) for i in map(reversed, reversed(key))], # list 안에 list
            list(reversed(list(zip(*key))))] # list 안에 tuple
    
    m, n = len(key), len(lock)
    # 확대된 lock 안에서 원래 lock의 위치를 위해서
    lock_end = 2*n
    # key가 lock보다 작거나 같으므로, big_lock에서 key가 위치할 범위 지정
    big_start, big_end = n - m + 1, 2 * n
    # lock을 상하좌우로 3배씩 확대. 즉 총 9개의 lock이 만들어짐
    big_lock = [lock[j] * 3 for i in range(3) for j in range(n)]
    
    for k in keys:
        if unlock(m, k, n, lock_end, big_start, big_end, big_lock):
            return True

    return False


# 2. 예전 Code
## 예전 코드에서 keys만 오늘 코드로 바꿈: 테스트 27 〉544.69ms -> 349.30ms
def solution(key, lock):
    # 0도, 90도, 180도, 270도 key들
    keys = [key,
            list(zip(*reversed(key))), # list 안에 tuple
            [list(i) for i in map(reversed, reversed(key))], # list 안에 list
            list(reversed(list(zip(*key))))] # list 안에 tuple
    
    n, m = len(lock), len(key) # lock: n * n, key: m * m
    
    # 상하좌우 3배(=9배) 넓어진 locks)]
    locks = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(n, 2 * n): # locks의 중앙에 lock을 위치시킴
        locks[i][n:2 * n] = lock[i - n]
        
    now_lock = [x[:] for x in locks] # 원본 보존용으로 locks 깊은복사
    
    for now_key in keys: # key를 돌려가며
        
        # x와 y를 이동해가며 key로 lock이 열리는지 확인하기
        for x in range(1, 2 * n):
            for y in range(1, 2 * n):
                for a in range(x, x + m): # 현재 위치의 key와 lock을 맞춰보기
                    now_lock[a][y:y + m] = map(lambda a, b: a + b, now_lock[a][y:y + m], now_key[a - x])
    			
                # lock이 key로 열린다면(lock의 홈 + key의 돌기 = 1)
                if set(sum(map(lambda x: x[n:2 * n], now_lock[n:2 * n]), [])) == {1}:
                    return True      
                
                now_lock = [x[:] for x in locks] # now_lock 초기화
    
    return False
           
                                               
'''
# Result
풀이 시간: 1시간
테스트 11 〉통과 (322.78ms, 10.3MB)
'''