'''
# 백준_16918_봄버맨. 실버 1. 풀이: 23.07.11 -> 실패 -> 성공

# How to
0초: 초기 상태: 폭탄 설치
1초: 아무것도 안함
2초: 나머지 폭탄 설치
3초: 0초의 폭탄 폭발
4초: 나머지 폭탄 설치
5초: 2초의 폭탄 폭발
...

- 짝수 시간: 모두 폭탄
- 홀수 시간만 별도로 폭발 반복
    - 1초 후 남은 폭탄 -> 3초에 터짐, 남은 폭탄 -> 5초에 터짐
    

## 반례
- 폭탄은 동시에 폭발한다.
    - 순차적으로 원본 배열을 빈칸으로 만들다가는, 실패하게 된다.

- 1초일 때: 초기 상태
- 짝수 시간일 때: 모두 폭탄
- 홀수 시간일 때:
    - n % 2 == 3일 때: 초기 상태에서 폭탄이 한 번 터진 상태
    - n % 2 == 1일 때(1초는 제외): 초기 상태에서 폭탄이 두 번 터진 상태

- 예제에서는 1초가 3, 7, 11..과 같지만, 반례에서 다른 경우가 있다.
    - 폭발로 모든 좌표가 빈칸이 되는 경우
배열: O.
1초 답: O.
2초 답: OO
3초 답: ..
4초 답: OO
5초 답: OO
6초 답: OO
7초 답: ..
8초 답: OO
9초 답: OO

# 리뷰
- 처음에는 bfs로 풀었는데, 폭탄을 순차적으로 터트리는 바람에 실패했다.
- 그 후에 규칙을 찾아봤지만, 1초는 홀수 시간과 별도인 것을 모르고 헤맸다.
    - 결국 질문게시판에서 반례를 보고 1초와 홀수 규칙과 다르다는걸 알게 되었다.
    - 근데 이를 규칙대로 구현하지 못하고, 그냥 홀수 시간 때 폭발을 반복해서 성공했다.
- 다른 사람 풀이를 보니, 다들 규칙대로 구현해서 훨씬 빨랐다.
    - 3, 7, 11..은 폭탄이 한번 터진 것, 5, 9, 13..은 폭탄이 두번 터진 것이었다.
    - 결국 규칙만 찾으면 쉽게 풀리는 문제였다..
- 아무리 봐도 bfs/dfs 문제가 아니라, 그냥 구현 문제 같다.
    - 다른 사람 풀이를 봐도 bfs나 dfs로 푼 사람은 없었다.
    - bfs로 풀 수는 있겠지만, 시간이 오래걸릴 것 같다.    
'''

# Code
# 성공
## 메모리: 33664 KB, 시간: 944 ms
import sys
input = sys.stdin.readline

# 격차판: r*c, n초
r, c, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

def solve(graph):        
    # 폭탄의 좌표 기록
    def bombs_list():
        new_bombs = []
        for x in range(r):
            for y in range(c):
                if graph[x][y] == 'O':
                    new_bombs.append((x, y))
    
        return new_bombs
    
    # 폭탄 폭발: 폭탄 -> 폭발 후 빈칸이 됨
    def explode_bombs():
        new_graph = [['O']*c for _ in range(r)]
        while bombs:
            x, y = bombs.pop()
            new_graph[x][y] = '.'
            for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                nx = x + i
                ny = y + j
                if 0 <= nx < r and 0 <= ny < c:
                    new_graph[nx][ny] = '.'

        return new_graph
    
    # 3, 5, 7.. 홀수 시간에만 폭발
    for _ in range(n // 2):
        bombs = bombs_list()
        graph = explode_bombs()
        
    return graph
    
# 짝수 초: 모든 칸이 폭탄인 상태로 출력
if n % 2 == 0:
    for _ in range(r):
        print('O'*c)
        
# 홀수 초:
else:
    for row in solve(graph):
        print(''.join(row))
