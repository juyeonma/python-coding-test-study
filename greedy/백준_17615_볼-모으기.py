'''
# 백준_17615_볼 모으기. 실버 1. 풀이: 23.05.30

# How to
- 한쪽에 공이 몰려있으면, 나머지만 이동하면 된다.
- 양 끝에 자신의 색이 없으면, 공 갯수만큼 이동한다.
- 한 종류만 있거나 공이 2개 이하면, 옮길 필요 없다.


# Review
- 처음에 양 끝이 같은 색일 경우를 고려하지 못해서 틀렸다.
    - 반례를 넣어서 찾았다..
    - 공의 갯수를 정답 list에 추가해서 해결.
- 이후 strip()을 이용한 간단한 코드를 발견했다.
    - 내 코드에서는 index를 이용해서 한쪽에 몰린 갯수를 제외한 나머지를 셌다.
    - 그러나 rstrip(), lstrip()을 사용하면 바로 양 끝을 제거할 수 있다.
    - 이렇게 되면 양 끝에 한 종류의 색만 있는 경우도 고려할 수 있어서 좋다.
'''

# 성공 Code
n = int(input())
ball = input()

# 한 종류만 있거나 공이 2개 이하면, 옮길 필요 없음
if len(set(ball)) == 1 or n <= 2:
    print(0)

else:
    ball_reverse = ball[::-1]
    
    r_cnt = ball.count('R')
    b_cnt = ball.count('B')
    
    # 양 끝이 같은 색일 경우를 고려하여, 각 공의 갯수를 정답 후보에 추가.
    answer = [r_cnt, b_cnt]
    
    for i in [ball, ball_reverse]:
        # 원래 list건 뒤집힌 list건, 첫번째 공을 제외한 개수가 곧 이동 횟수
        if i[0] == 'R':
            answer.append(r_cnt - i.index('B'))
            
        else: # B
            answer.append(b_cnt - i.index('R'))

    print(min(answer))
    
    
# 구글링: 좋은 Code
# 출처: https://velog.io/@doyun/백준-17615-볼-모으기

n = int(input())
balls = input()

cnt = []

# 오른쪽에 몰린 공을 제외한 갯수가 곧 이동 횟수
cnt.append(balls.rstrip('R').count('R'))
cnt.append(balls.rstrip('B').count('B'))

# 왼쪽에 몰린 공을 제외한 갯수가 곧 이동 횟수
cnt.append(balls.lstrip('R').count('R'))
cnt.append(balls.lstrip('B').count('B'))

print(min(cnt))


'''
# Result
풀이 시간: 1시간
메모리: 32236 KB
시간: 64 ms
코드 길이: 495 B
'''