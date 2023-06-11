
#먼저 Enter와 Change에서 닉네임이 바뀔수 있으므로 전체 record를 돌면서 해당 uid의 닉네임을 dict에 넣어준다.
#다시 record를 돌면서 enter와 leave만 기록하면 되는데 이 때 맨 마지막으로 바뀐 이름을 기록해야하므로 dict에서 탐색하며 바꿔주면서 넣어준다.

def solution(record):
    answer = []
    check={}
    for s in record:
        if len(s.split())==3:
            status,uid,name=s.split()
        else:
            status,uid=s.split()
        if status=="Enter" or status=="Change":
            check[uid]=name
            
    for s in record:
        if len(s.split())==3:
            status,uid,name=s.split()
        else:
            status,uid=s.split()
        if status=="Enter":
            answer.append(f'{check[uid]}님이 들어왔습니다.')
        elif status=="Leave":
            answer.append(f'{check[uid]}님이 나갔습니다.')
    return answer

# 14분

# 위 풀이 다듬기
def solution(record):
    answer = []
    check={}
    for s in record:
        if len(s.split())==3:
            status,uid,name=s.split()
            if status=="Enter" or status=="Change":
                check[uid]=name
            
    for s in record:
        ss=s.split()
        status =ss[0]
        uid=ss[1]
        if status=="Enter":
            answer.append(f'{check[uid]}님이 들어왔습니다.')
        elif status=="Leave":
            answer.append(f'{check[uid]}님이 나갔습니다.')
    return answer


# 이렇게도 가능하다
def solution(record):
    answer=[]
    check={}
    for s in record:
        if s.startswith("E") or s.startswith("C"):
            _,uid,name=s.split()
            check[uid]=name
            
    for s in record:
        uid = s.split()[1]
        if s.startswith("E"):
            answer.append(f'{check[uid]}님이 들어왔습니다.')
        elif s.startswith("L"):
            answer.append(f'{check[uid]}님이 나갔습니다.')
    return answer