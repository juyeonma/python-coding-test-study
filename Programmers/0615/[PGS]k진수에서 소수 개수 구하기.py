# 시간복잡도 O(n)..? => 근데 이중 포문이 돌아가네...ㅎ..
# 어떤 알고리즘? 구현이라고 생각하고 풀이
# 풀이 시간 : 28분

# 진수로 바꿔주기
def change(n, k):
    ch = ''
    while n > 0:
        ch += str(n % k)
        n //= k
    return ch[::-1]
# 소수 찾기
def prime(n):
    if n == '1':
        return False
    for i in range(2, int(int(n)**(1/2))+1):
        if int(n) % i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    s = change(n, k)
    number = ' '.join(s.split('0')).split()
    for n in number:
        if prime(n):
            answer += 1
    return answer
print(solution(437674, 3))

# 시간(제일 빠른 시간, 제일 느린 시간만 가져옴)
# 테스트 1 〉	통과 (249.42ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)

# 다른 사람의 풀이 => 접근법이 나랑 거의 비슷해서 놀랬다..!
# 보완해야할 점 : prime(int(n)) 으로 넣었다면 더 편했을 것 같다