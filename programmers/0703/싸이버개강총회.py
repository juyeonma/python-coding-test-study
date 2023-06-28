import sys
input = sys.stdin.readline
s,e,q = map(str,input().split())
s = int(s[:2]+s[3:])
e = int(e[:2]+e[3:])
q = int(q[:2]+q[3:])

student = set()
cnt = 0
#입력갯수가 정해지지 않았을 때 쓸것!
while True:
    try:
        time,name = map(str,input().split())
        time=int(time[:2]+time[3:])
        if time<=s: #시작 전에 채팅기록이 있다면 출석한것으로 포함
            student.add(name)
        if time>=e and time<=q and name in student: #수업이 끝나고, 스트리밍이 끝날때까지 기록이 있다면 출석한것
            student.remove(name) #그 학생들을 제거하면서
            cnt+=1 #숫자를 카운트
    except:
        break
print(cnt)

# 메모리 : 43548 KB
# 시간 : 196 ms
# 코드길이 : 451 B