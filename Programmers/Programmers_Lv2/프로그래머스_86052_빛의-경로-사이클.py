'''
# 프로그래머스_86052_빛의 경로 사이클. Lv 2. 풀이: 23.06.07 -> 실패

# How to
- 동서남북 모든 방향에서 노드로 들어올 때, 각 노드에서 출발
- 매번 방향과 좌표를 갱신
- 처음 좌표와 방향으로 돌아왔을때, 기록
- 기록이 정답의 기록들과 같다면 +1 하고, 기록*2를 정답에 추가

## 반례
["S", "S"] = [1,1,1,1,2,2]
초기좌표 방향 => 답
0, 0 left =>1
0, 0 right =>1
0, 0 up => 2
0, 0 down =>2
1, 0 left =>1
1, 0 right => 1

오름차순 [1,1,1,1,2,2]


# Review
- 규칙이 있는걸까? 아니면 그냥 쌩 구현? 완전탐색?
- 구현에서 실패.. 왜 실패했는지 디버깅을 해봐야겠다ㅠㅠ
'''

# Code

'''
S, L, R = 0, -1, 1

'''
# 실패 Code
def solution(grid):
    answer = []
    # n*m 배열
    n, m = len(grid), len(grid[0])
    
    # grid = list(map(lambda x: list(x), grid)) 와 동일
    grid = [list(i) for i in grid]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    start = [n-1, 0, 0, m-1]
    dic = {'S': 0, 'L': -1, 'R': 1}
    result = []
    
    # tmp 리스트, reuslt 리스트
    def check(list1, list2):
        if len(list1) > len(list2):
            return False
        for i in range(len(list2)-n+1):
            if list2[i:i+n] == list1:
                return True
        return False
    
    for d in range(4):
        sd = d
        if dx[d] != 0:
            x = start[d]
            tmp = []
            cnt = 0
            for y in range(m):
                sx, sy = x, y
                while True:
                    d = (d+dic[grid[x][y]])%4
                    x, y = (x+dx[d])%n, (y+dy[d])%m
                    cnt += 1
                    tmp.append((x, y))
                    if x == sx and y == sy and d == (sd+dic[grid[sx][sy]])%4:
                        break
                if not result:
                    result.append(tmp*2)
                    answer.append(cnt)
                else:
                    for j in result:
                        if check(tmp, j):
                            result.append(tmp*2)                      
                            answer.append(cnt)
                            break
                        
        elif dy[d] != 0:
            y = start[d]
            for x in range(n):
                sx, sy = x, y
                while True:
                    d = (d+dic[grid[x][y]])%4
                    x, y = (x+dx[d])%n, (y+dy[d])%m
                    cnt += 1
                    tmp.append((x, y))
                    if x == sx and y == sy and d == sd:
                        break
                if not result:
                    result.append(tmp*2)
                    answer.append(cnt)
                else:
                    for j in result:
                        if check(tmp, j):
                            result.append(tmp*2)                      
                            answer.append(cnt)
                            break
    return answer


'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''