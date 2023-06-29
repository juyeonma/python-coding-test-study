import sys
input = sys.stdin.readline
s, e, q = input().split()

start = []
end = []
s_hour, s_min = map(int, s.split(":"))
e_hour, e_min = map(int, e.split(":"))
q_hour, q_min = map(int, q.split(":"))
while True:
    try:
        time, name = input().split()
        time_hour, time_min = map(int, time.split(":"))
        if time_hour < s_hour:
            start.append(name)
        elif time_hour == s_hour and s_min <= time_min:
            start.append(name)
        elif e_hour < time_hour < q_hour:
            end.append(name)
        elif (e_hour == time_hour and e_min <= time_min):
            if (time_hour < q_hour) or (time_hour == q_hour and q_min >= time_min):
                end.append(name)
        elif q_hour == time_hour and q_min >= time_min:
            end.append(name)
    except:
        break
print(len(set(start) & set(end)))

# 틀림 => 반례도 못찾았다.. 어디서 틀린거지..ㅠㅠ.. => 좀 더 포괄적으로 짜야겠다..


# 다른 풀이 참고
import sys
input = sys.stdin.readline

start, end, stream = input().split()
start = int(start[:2] + start[3:])
end = int(end[:2] + end[3:])
stream = int(stream[:2] + stream[3:])

attend = set()
cnt = 0

while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= start:
            attend.add(name)
        elif end <= time <= stream and name in attend:
            attend.remove(name)
            cnt += 1
    except:
        break

print(cnt)