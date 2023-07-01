'''
# 백준_19583_싸이버개강총회. 실버 2. 풀이: 23.06.27

# How to
- 입장 & 퇴장 모두 만족한 학회원 수?
- 입장 체크: 개강총회 시작시간 이하에 채팅 여부
- 퇴장 체크: 개강총회 종료시간 이상 ~ 스트리밍 종료시간 이하에 채팅 여부

- 시:분을 :을 빼고 4자리 수로 만들어서, 비교


# Review
- "노트: 문제의 설명은 사실과 다르다." 는 무슨 뜻일까?
- 무조건 "시:분"의 문자열을 정수형으로 바꾸어야 한다고 생각했는데, 맞힌 사람을 보니까 그냥 문자열 상태로 비교했다.
    - 즉 ':'가 존재해도 크기비교가 가능하다.
    - 당연한건데, 왜 풀때는 정수형에 사로잡혔지..?
'''

# 성공 Code
import sys
input = sys.stdin.readline

start, end1, end2 = map(lambda x: int(x.replace(':', '')), input().rstrip().split())

check = set()
answer = 0
while True:
    try:
        t, name = input().rstrip().split()
        t = int(t.replace(':', ''))
        
        # 입장 체크
        if t <= start:
            check.add(name)
        
        # 퇴장 체크
        elif end1 <= t <= end2 and name in check:
            answer += 1
            check.remove(name)
        
    except:
        break

print(answer)


# 실패: 시와 분을 나누는 바람에, 조건을 체크하기가 까다로워짐.
import sys
input = sys.stdin.readline

start, end1, end2 = input().rstrip().split()
start_h, start_m = map(int, start.split(':'))
end1_h, end1_m = map(int, end1.split(':'))
end2_h, end2_m = map(int, end2.split(':'))

check = set()
answer = 0
while True:
    try:
        t, name = input().rstrip().split()
        h, m = map(int, t.split(':'))
        
        # 입장 체크
        if h < start_h  or (h == start_h and m <= start_m):
            check.add(name)
        
        # 퇴장 체크: 틀린 부분이 있음
        elif ((end1_h <= h < end2_h) or (h == end2_h and m <= end2_m)) and (name in check):
            answer += 1
            check.remove(name)
    except:
        break
        
print(answer)


'''
# Result
풀이 시간: 30분
메모리: 43680 KB
시간: 140 ms
코드 길이: 473 B
'''