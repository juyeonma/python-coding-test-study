'''
# 프로그래머스_92344_파괴되지 않은 건물.py. Lv 3. 풀이: 23.06.18 -> 실패

# How to
- 3가지 방법을 시도(사실 다 같긴 한데..) -> 실패
1. 매번 건물 파괴 여부 기록
2. 표적 좌표만 기록 후, 검사
3. 공격 or 회복만 기록한 후, 한꺼번에 적용

- 모범답안: 누적합 이용
추후 다시 풀기


# Review
- 어떤 알고리즘인지 도저히 생각나지 않았다.
    - 입력을 보니 시간초과가 뻔했지만, 별다른 도리가 없었다.
    - 그냥 하나하나 좌표를 보는 방법 말고 뭐가 있을까?
    - 나름 변주를 준다고 표적 좌표만 기록하기도 해봤지만, 역시나 효율성 실패.
    - 애초에 근본적으로 좌표를 하나하나 탐색하는걸 고치지 않는 이상 시간초과는 당연했다.
    
- 도대체 이게 무슨 알고리즘일까? 너무 궁금해서 찾아보니, "누적합"이 답이었다.
- 참고:
    https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/#문제-6-파괴되지-않은-건물
    https://school.programmers.co.kr/questions/30876
    https://school.programmers.co.kr/questions/25471
    
- 결국 2차원 배열을 내가 원하는 형태로 조작하는 것이 스킬이구나..    
- 단번에 이해되지 않았으므로, 차근차근 살펴봐야겠다.
'''


# 1. 매번 건물 파괴 여부 기록: 효율성 테스트 실패
## 정확성 테스트 10 〉통과 (20.86ms, 10.4MB), 효율성 테스트: 시간 초과
def solution(board, skill):
    n, m = len(board), len(board[0])
    check = [[True]*m for _ in range(n)]
    
    for t, r1, c1, r2, c2, d in skill:
        # 공격이면, 내구도 감소
        if t == 1:
            d *= -1
        # 해당하는 좌표를 탐색하며, 공격 or 회복
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                board[x][y] += d
                # 건물 파괴 여부 기록
                if board[x][y] <= 0:
                    check[x][y] = False
                else:
                    check[x][y] = True
                    
    # 파괴되지 않은 건물의 개수를 return
    return sum(map(sum, check))


# 2. 표적 좌표만 기록 후, 검사: 효율성 테스트 실패
## 정확성 테스트 10 〉	통과 (23.65ms, 11.3MB), 효율성 테스트: 시간초과
def solution(board, skill):
    n, m = len(board), len(board[0])
    check = set()
    for t, r1, c1, r2, c2, d in skill:
        # 공격이면, 내구도 감소
        if t == 1:
            d *= -1
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                board[x][y] += d
                # 표적 좌표만 기록
                check.add((x, y))
                
    answer, result = n*m, 0
    # 표적 좌표만 검사해서 파괴된 건물의 개수를 센다.
    for x, y in check:
        if board[x][y] <= 0:
            result += 1
            
    # 전체 건물의 개수 - 파괴된 건물의 개수 = 파괴되지 않은 건물의 개수
    return answer - result


# 3. 공격 or 회복만 기록한 후, 한꺼번에 적용: 효율성 테스트 실패
## 정확성 테스트 10 〉통과 (28.84ms, 11.1MB), 효율성 테스트: 시간초과
def solution(board, skill):
    n, m = len(board), len(board[0])
    check = {}
    for t, r1, c1, r2, c2, d in skill:
        # 공격이면, 내구도 감소
        if t == 1:
            d *= -1
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                if (x, y) in check:
                    check[(x, y)] += d
                else:
                    check[(x, y)] = d
                
    answer, result = n*m, 0
    for x, y in check:
        if check[(x, y)] + board[x][y] <= 0:
            result += 1
        
    return answer - result


'''
# Result
풀이 시간: 실패

'''