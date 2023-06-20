'''
# 프로그래머스_42884_단속카메라. Lv 3. 풀이: 23.06.09

# How to
- 차량이 많이 겹칠수록, 필요한 카메라도 적다.
- 진입 지점으로 정렬한다.
- 첫 차량의 진입~진출 구간을 카메라 설치 start~end 구간으로 설정하고, 우선 카메라를 한대 설치한다(answer = 1)
- 매번 차량이 카메라 구간과 겹치는지 판단한다.
- 겹치면, start와 end를 갱신한다.
    - 현재 차량의 진입이 start가 된다.
    - end 갱신이 고민이었는데, 제일 빨리 들어와서 제일 늦게 나가는 반례를 생각하면,
    현재 차량의 진출과 end 중 작은 값이 end가 된다.
- 겹치지 않으면, 새로운 카메라를 설치한다.
    - 즉 현재 차량의 진입~진출이 새로운 start~end가 된다.
    - 그리고 카메라를 하나 더 설치한다(answer += 1)

## 반례
- 첫번째 진입 차량이 마지막으로 진출할 때.
[[-20, 100], [-14,-5], [-18,-13], [-5,-3]]	
답: 2

# Review
- 반례를 뒤늦게 생각해서 시간이 소모 되었지만, 코드 자체는 쉽다. 그런데.. 코드가 느리다.
- 다른 사람 풀이를 보니, 진입이 아니라 진출로 정렬하는 것이 포인트였다.
- 다른 사람 풀이 1번은 진출을 기준으로 정렬 했는데, 그 이유가 질문게시판에 있었다.
    - 출처: https://school.programmers.co.kr/questions/27135
    - 키 포인트는 "카메라는 먼저 진출한 지점 순서대로 설치되어야한다."
    - 이유: 현재 진출지점이 절대로 현재 카메라의 위치를 넘는 경우는 존재하지 않기 때문
    - 따라서, 진출로 정렬하고, 진입위치가 현재 카메라의 위치만 넘었는지만 판단한다.진출
- 다른 사람 풀이 2번 또한 1번과 같은 로직이지만, 다만 뒤집었을 뿐으로 보인다.
'''

# 성공 Code
def solution(routes):
    routes.sort()
    # 첫번째 차량의 진입~진출이 곧 카메라 설치 구간이 된다.
    # 즉 우선 카메라 1대 설치
    answer = 1
    start, end = routes[0]
    for a, b in routes:
        # 현재 차량과 카메라 구간이 겹친다면,
        if a in range(start, end+1):
            start, end = a, min(end, b)
            
        # 겹치지 않다면,
        else:
            start, end = a, b
            answer += 1
    return answer


# 다른 사람 풀이
## 1. 진출 시간으로 오름차순 정렬
## 효율성 테스트: 테스트 5 〉통과 (0.96ms, 10.6MB)
def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001
    # 현재 카메라의 설치 구간 < 진입 구간
    for route in routes:
        if last_camera < route[0]:
            # 카메라 한대 더 설치하고
            answer += 1
            # 현재 카메라의 위치를 종점 위치로 갱신
            last_camera = route[1]
    return answer


## 2. 진입 시간으로 내림차순 정렬
## 효율성 테스트: 테스트 3 〉통과 (1.44ms, 10.5MB)
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0], reverse=True) 
    camera = 30001 
    for route in routes:
        if camera > route[1]:
            answer += 1
            camera = route[0]
    return answer


'''
# Result
풀이 시간: 30분
- 정확성 테스트
테스트 3 〉	통과 (0.08ms, 10.3MB)

- 효율성 테스트
테스트 5 〉	통과 (7.76ms, 10.4MB)
'''