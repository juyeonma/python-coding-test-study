'''
# 프로그래머스_62048_멀쩡한 사각형. Lv 2. 풀이: 23.06.21 -> 실패 -> 성공

# How to
## 1. 내 풀이
- 가로, 세로 길이의 최대공약수만큼 도형이 반복된다.
- 대각선 규칙: 가로 + 세로 - 1 만큼 대각선에 걸친다.
- 전체 대각선 걸친 개수 = 전체 개수 - 최대공약수 * (작은 사각형의 대각선 걸친 개수)

## 2. 다른 사람 풀이
- 유클리드 호제법으로 최대공약수를 구함

# Review
- 문제를 잘못 골랐나보다.. 코딩테스트가 아니라 수학 문제였다..
- 최대공약수는 알겠는데, 대각선 규칙을 몰라서 질문 게시판을 보았다.
- 나는 최대공약수를 그냥 모든 숫자를 탐색해서 구했는데, 그게 아니라 math에 gcd 함수도 있었고, 다른 사람 풀이처럼 유클리드 호제법으로 구할 수도 있는 거였다.
- 유클리드 호제법
    2개의 자연수 a, b (a > b)
    a를 b로 나눈 나머지를 r이라고 했을때, GCD(a, b) = GCD(b, r)
    예: GCD(24,16) = GCD(16,8) = GCD(8,0) : 최대공약수 = 8
'''

# Code
def solution(w,h):
    answer = w * h
    cnt = 1
    
    # 정사각형이면, 바로 return
    if w == h:
        return answer - h
    
    # 최대공약수 구하기
    for i in range(max(w, h)//2, 1, -1):
        if not w%i and not h%i:
            w, h = w//i, h//i
            cnt = i
            break
    
    # 전체 개수 - 최대공약수 * (작은 사각형의 대각선 걸친 개수)
    answer -= cnt * (w + h - 1)
    
    return answer


# 다른 사람 풀이(가독성 있게 수정)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def solution(w, h): 
    return w * h - (w + h - gcd(w, h))


'''
# Result
풀이 시간: 실패 -> 20분
테스트 13 〉통과 (3479.19ms, 10MB)
'''