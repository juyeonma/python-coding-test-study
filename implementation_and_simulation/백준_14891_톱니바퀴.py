'''
# 백준_14891_톱니바퀴. 골드 5. 풀이: 23.06.29

# How to
- 맞닿는 부분: (arr_i[2], arr_i+1[6]): (1과 2), (2와 3), (3과 4)
- 시계 방향 회전: arr = arr[-1] + arr[:-1]
- 반시계 방향 회전: arr = arr[1:] + arr[0]

- 1. 현재 톱니바퀴들의 맞닿은 부분을 딕셔너리로 만든다.
    - 같은 극이면 True, 다른 극이면 False
- 2. 현재 톱니바퀴를 회전시킨다.
    - 시계 방향 회전: arr = arr[-1] + arr[:-1]
    - 반시계 방향 회전: arr = arr[1:] + arr[0]
- 3. 옆 톱니바퀴들도 회전시킨다.
    - 왼쪽, 오른쪽 나누어서
    - 매번 현재 바퀴와 왼쪽/오른쪽 바퀴를 갱신하고, 회전방향은 음수를 곱하며 갱신
    - 맞닿은 부분이 같은 극이면, 중단
- 4. 모든 회전이 끝나면, 12시 방향의 값을 각각 가중치만큼 곱해서 합한다.
    - 각각 가중치가: 1, 2, 4, 8 -> i번 바퀴의 가중치는 2^(i-1)


# Review
- 풀이 시간이 너무 오래 걸리면 중단하고 답을 보기로 했는데, 이번에도 1시간 30분이나 소요했다.
- 하나만 찾으면 풀거 같단 생각에 한 문제만 붙잡고 시간을 오래 쏟는 버릇을 고쳐야할거 같은데..
    - 정말 그 하나만 찾으면 문제가 바로 해결되어서 자꾸 이런일이 반복된다.
    - 먼저 맞닿은 부분을 구한 다음에 회전을 시켜야하는데, 이 부분을 놓쳐서 대부분의 시간을 쏟았다..
- 어쩌다보니 각각 함수로 분리했는데, 분리하지 않으면 너무 코드가 지저분해져서 어쩔 수 없었다.
'''

# Code
# 맞닿은 부분: 같은 극인가? True, 다른 극인가? False
def contact_part(dic):
    return {(i, i+1): dic[i][2] == dic[i+1][6] for i in range(1, 4)}

# 현재 톱니바퀴 회전
def rotate(num, dir, dic):
    # 시계 방향 회전
    if dir == 1:
        dic[num] = dic[num][-1] + dic[num][:-1]
        
    # 반시계 방향 회전
    else:
        dic[num] = dic[num][1:] + dic[num][0]

# 옆 톱니바퀴들 회전
def rotate_next(num, dir, dic, contact_dic):
    # 왼쪽으로
    now, left_d = num, -dir
    for left in range(num-1, 0, -1):
        # 맞닿은 부분이 같은 극이면, 중단
        if contact_dic[(left, now)]:
            break
        # 왼쪽 바퀴 회전시키고, 톱니바퀴 번호와 회전 방향 갱신
        rotate(left, left_d, dic)
        now, left_d = left, -left_d

    # 오른쪽으로
    now, right_d = num, -dir
    for right in range(num+1, 5):
        # 맞닿은 부분이 같은 극이면, 중단
        if contact_dic[(now, right)]:
            break
        # 오른쪽 바퀴 회전시키고, 톱니바퀴 번호와 회전 방향 갱신
        rotate(right, right_d, dic)
        now, right_d = right, -right_d
        
        
# 1~4번 톱니바퀴. N극은 0, S극은 1
dic = {1: input(), 2: input(), 3: input(), 4: input()}    

for _ in range(int(input())):
    # 회전시킨 톱니바퀴의 번호, 회전 방향(1: 시계 방향, -1: 반시계 방향)
    num, dir = map(int, input().split())
    # 맞닿은 부분 딕셔너리: 같은 극인가?
    contact_dic = contact_part(dic)
    # 현재 톱니바퀴 회전시키고
    rotate(num, dir, dic)
    # 옆 톱니바퀴들도 회전
    rotate_next(num, dir, dic, contact_dic)

# 12시 방향(즉 0번 인덱스) 각각 가중치만큼 합하기: i번 바퀴의 가중치는 2^(i-1)
# print(int(dic[1][0]) + int(dic[2][0])*2 + int(dic[3][0])*4 + int(dic[4][0])*8)과 같음
print(sum(int(v[0]) * 2**(k-1) for k, v in dic.items()))


'''
# Result
풀이 시간: 1시간 30분
메모리: 31256 KB
시간: 48 ms
코드 길이: 1565 B
'''