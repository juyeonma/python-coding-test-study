'''
# 백준_20436_ZOAC 3. 실버 4. 풀이: 23.06.29

# How to
행: 3
열: 위에서부터 10, 9, 7
- 각 키의 행, 열 딕셔너리를 만든다.
    - 각 행의 길이가 다르므로, 행마다 문자열로 만들어서 리스트에 담고, 이중 for문으로 딕셔너리 만들기
- 왼손, 즉 한글 자음쪽 자판의 키만 따로 저장한다.
- 매번 입력할 좌표가 왼손인지 오른손인지 판단한다.
- 현재 좌표와 입력할 좌표 사이의 거리를 잰 후, 
    - 거리 +1을 정답에 더하고, 현재 좌표를 갱신한다.

# Review
- 딕셔너리에서 일일히 키를 입력해도 되지만, 너무 길어진다.
- 람다로 하려다가 그냥 이중 for문으로.. 
'''

# 성공 Code
# 각 키의 행, 열 딕셔너리 만들기
k_str = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
dic = {k: (r, c) for r, i in enumerate(k_str) for c, k in enumerate(i)}

# 한글 자음 쪽 자판(=왼손)
left_str = set([*'qwertasdfgzxcv'])

# 처음 왼손, 오른손이 위치한 키와 좌표
left, right = input().split()
left_r, left_c = dic[left]
right_r, right_c = dic[right]

answer = 0
for s in input():
    r, c = dic[s]
    # 왼손으로 해야할 경우
    if s in left_str:
        # 입력할 좌표와 현재 왼손 좌표간의 거리 + 1을 정답에 더하고, 왼손 좌표 갱신
        answer += abs(r-left_r) + abs(c-left_c) + 1
        left_r, left_c = r, c

    # right_str: 오른손으로 해야할 경우
    else:
        # 입력할 좌표와 현재 오른손 좌표간의 거리 + 1을 정답에 더하고, 오른손 좌표 갱신
        answer += abs(r-right_r) + abs(c-right_c) + 1
        right_r, right_c = r, c
        
print(answer)


'''
# Result
풀이 시간: 15분
메모리: 31388 KB
시간: 40 ms
코드 길이: 531 B
'''