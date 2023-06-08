'''
# 프로그래머스_오픈채팅방. Lv 2. 풀이: 23.06.08

# How to
- 그냥.. 구현..
- 입장이면, 아이디와 enter를 리스트에 추가. 아이디 딕셔너리에 닉네임 갱신
- 퇴장이면, 아이디와 leave를 리스트에 추가
- 변경이면, 아이디 딕셔너리에 닉네임 갱신

# Review
- 그냥 구현..
- 다른 사람 풀이 -> 나중에 보기. 시간이 얼마나 단축될까 궁금
'''

# 성공 Code
def solution(record):
    answer = []
    id_list = {}
    inout_list = []
    for i in record:
        now = list(i.split())
        if now[0] == 'Enter':
            inout_list.append([now[1], 'enter'])
            id_list[now[1]] = now[2]
            
        elif now[0] == 'Leave':
            inout_list.append([now[1], 'leave'])
            
        else:
            id_list[now[1]] = now[2]
    
    for u, a in inout_list:
        user = id_list[u]
        if a == 'enter':
            answer.append(f'{user}님이 들어왔습니다.')
        else:
            answer.append(f'{user}님이 나갔습니다.')
        
    return answer

# 다른 사람 풀이 -> 나중에 보기. 시간이 얼마나 단축될까 궁금
## 1. 가장 심플?
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

## 2. 숏코딩.. 두줄..
'''
처음 풀이하는데 있어서 Enter에 대해 먼저 dict를 만들고 Change에 대해 dict를 만들어서 에러가 발생
다음 반례를 생각해보길,
1.prodo 입장 ->
2.prodo에서 ryan으로 Change ->
3.prodo 퇴장 ->
4.prodo로 재입장

return ['prodo 입장','prodo 퇴장','prodo 입장']

Change가 최종적인 닉네임이 아님,,
재입장시에도 닉네임변경이 가능하다는 것을 배제하고 풀어서 틀린 것.
'''
def solution(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]


'''
# Result
풀이 시간: 10분
테스트 26 〉통과 (128.60ms, 44.1MB)
'''