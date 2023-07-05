'''
# 백준_ 20056_마법사 상어와 파이어볼. 골드 4. 풀이: 23.06.30

# How to
- 원형: 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.

- 초기 파이어볼 딕셔너리에 기록한다.
- k번 이동하며 배열을 갱신한다.
    - 따로 함수로 빼서 문제 그대로 1, 2 단계를 차례대로 진행한다.
    - 이때 새로운 딕셔너리를 만들어서 기록하고, 마지막에 return 한다.
    - 2단계에서 질량이 0일 때 바로 key를 삭제하지 말고, 소멸 key 목록에 저장 후 2단계가 끝난 다음에 key를 삭제한다.
- 남아있는 파이어볼 질량의 합을 출력한다.


## 예제
1 1 5 2 2
1 4 7 1 6

-> 1번 이동:
- 1.
0 0 5,7 0
0 0 0 0
0 0 0 0
0 0 0 0
- 2.
질량: (5+7)//5 = 2
속력: (2+1)//2 = 1
방향: 0, 2, 4, 6
정답: 2+2+2+2 = 8

-> 2번 이동:
- 1.
0 2 0 2
0 0 2 0
0 0 0 0
0 0 2 0
- 2.
한 칸에 2개 이상 있는게 없음
정답: 2+2+2+2 = 8


## 반례
- "4. 질량이 0인 파이어볼은 소멸되어 없어진다."
-> 바로 del이나 pop으로 key를 지우면, 다음 에러가 뜸:
RuntimeError: dictionary changed size during iteration


# Review
- 문제를 꼼꼼히 읽지 않아서 시간 반절은 날렸다..ㅎ
- 오해 1. "1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다."를 이해 못했다.
    - 1번행 = N번행으로 오해하는 바람에 예제를 이해 못해서 얼마나 헤맸는지...ㅎ
- 오해 2. 방향d와 속력s를 거꾸로 봤다.. 
    - 문제는 "방향은 di, 속력은 si이다.", 입력은 "다섯 정수 ri, ci, mi, si, di"라고 적혀있어서 순서를 거꾸로 이해했다.
- 진짜진짜 문제를 꼼꼼히 읽고, 그대로 구현하는 습관을 길러야겠다ㅠㅠ

- 원래 기존 배열을 수정하려고 했지만, 너무 복잡해서 새로운 딕셔너리를 만들어서 매번 갱신했다.
- 또한 바로바로 질량 0인 key(즉 좌표)를 삭제하려 했지만, 에러가 뜨는 바람에 별도로 리스트에 저장 후 key를 지웠다.
'''

# 성공 Code
# 파이어볼을 이동해서 새로운 배열을 만듦
def make_new_dic(dic, dx, dy):
    new_dic = {}
    # 1. 자신의 방향 d대로 속력 s만큼 이동
    for (r, c), v in dic.items():
        for m, s, d in v:
            new_r = (r + dx[d]*s) % n
            new_c = (c + dy[d]*s) % n
            new_dic.setdefault((new_r, new_c), [])
            new_dic[(new_r, new_c)].append([m, s, d])

    # 2. 한 칸에 2개 이상의 파이어볼이 있다면,
    del_keys = []
    for (r, c), v in new_dic.items():
        if 2 <= len(v):
            # 2-3. 새로운 질량, 새로운 속력
            new_m = sum(i[0] for i in v) // 5
            new_s = sum(i[1] for i in v) // len(v)
            
            # 2-3. 새로운 방향: 방향이 모두 홀수이거나 짝수라면,
            # new_d = [0, 2, 4, 6] if len(set(i[2] % 2 for i in v)) == 1 else [1, 3, 5, 7]
            if len(set(i[2] % 2 for i in v)) == 1:
                new_d = [0, 2, 4, 6]
            else:
                new_d = [1, 3, 5, 7]
            
            # 2-4. 질량이 0이면 소멸 key 목록에 올리고, 0이 아니면 4개의 파이어볼로 나눔
            if new_m != 0:
                new_dic[(r, c)] = [[new_m, new_s, nd] for nd in new_d]
            else:
                del_keys.append((r, c))
                
    # 2-4. 질량이 0인 파이어볼은 소멸
    for r, c in del_keys:
        del new_dic[(r, c)]

    return new_dic

# n*n 격자, 파이어볼 m개, 이동 k번
n, m, k = map(int, input().split())
# 초기 파이어볼 기록
dic = {}
for _ in range(m):
    # 좌표: (r, c), 질량: m, 속력: s, 방향: d
    r, c, m, s, d = map(int, input().split())
    dic[(r-1, c-1)] = [[m, s, d]]

# 8칸의 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# k번 이동하며 배열을 갱신
for _ in range(k):
    dic = make_new_dic(dic, dx, dy)

# 남아있는 파이어볼 질량의 합을 출력
print(sum(m for v in dic.values() for m, _, _ in v))


'''
# Result
풀이 시간: 2시간 + @
메모리: 33300 KB
시간: 480 ms
코드 길이: 1916 B
'''