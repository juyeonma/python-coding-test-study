# 개강 총회전까지의 닉네임을 저장하고 개강총회 끝내고 스트리밍전까지의 닉네임을 찾아서 카운팅한다
# 처음 풀이는 시간과 닉네임을 저장한 뒤 다시 for문 돌려서 찾았는데 그럴필요없이 바로하면된다.
# 입력값을 input으로 받으면 시간초과가 난다

import sys

s,e,q = input().split()
start_time = int(s[:2]+s[3:])
end_time = int(e[:2]+e[3:])
quit_time = int(q[:2]+q[3:])
cnt = 0

records = []  
for line in sys.stdin:
    time,name = line.split()
    records.append((int(time[:2]+time[3:]),name))

check=set()
for record in records:
    if record[0]<=start_time:
        check.add(record[1])
    if quit_time>=record[0]>=end_time:
        if record[1] in check:
            check.remove(record[1])
            cnt+=1

print(cnt)

#메모리 54572kb 시간 188ms


import sys

s,e,q = input().split()
start_time = int(s[:2]+s[3:])
end_time = int(e[:2]+e[3:])
quit_time = int(q[:2]+q[3:])
cnt = 0
 
check=set()
for line in sys.stdin:
    time,name = line.split()
    time=int(time[:2]+time[3:])
    if time<=start_time:
        check.add(name)
    if quit_time>=time>=end_time:
        if name in check:
            check.remove(name)
            cnt+=1    

print(cnt)

#메모리 43548kb 시간 168ms

#입력값 받는 부분 찾아보다가 시간을 안쟀다.