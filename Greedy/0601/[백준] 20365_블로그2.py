# 최적의 방법을 생각해서 푸는 방법이 그리디라는데 이런게 그리디인가...
# 그냥 구현하는 것 같다.

# 나는 전체를 칠하고 줄여가면서 다른 색이 보이면 다시 그 범위만큼 연속적으로 칠하는 방식으로 풀었는데
# 다른 사람들 방식은 전체를 칠하고 다른 색깔로 칠해진 부분을 찾아서 그 부분만 따로 칠해주는 방식으로 풀었다.
# 접근 방식에 따라 풀이가 이렇게 달라지는구나..

# 먼저 하나의 색깔로 색칠을 한 뒤 첫번째인덱스와 마지막 인덱스를 설정해서 앞쪽에서 한칸씩 이동하며 다른 색깔이 될때까지 이동한다.
# 그 후 다른 색깔이되면 맨 뒤부터 한칸씩 당기면서 다른색깔이 되는 부분을 찾는다.
# 카운팅을 하고 위 과정을 반복한다.

n =int(input())
problem = input()
st=0 # 처음 인덱스
en=len(problem)-1 #마지막인덱스
cnt=1 # 처음에 하나로 전부 칠했을 때 카운팅
temp_color=problem[0] # 처음에 하나로 전부 칠했을 때의 색깔

while st<=en: # 모든 문제를 전부 다돌면 탈출
    if problem[st]==temp_color: # 앞쪽위치와 색깔이 같으면 인덱스 한칸 이동
        st+=1
    else: #앞쪽위치와 색깔이 다르면 뒷쪽인덱스 확인하기
        if problem[en]!=temp_color:  # 뒷쪽인덱스의 색과 현재 칠해진 색이 달라지면 카운팅하고 색전환, 앞쪽인덱스 한칸이동
            cnt+=1
            temp_color=problem[st]
            st+=1
        en-=1 #앞쪽이 다를 경우 뒷쪽이 같든 다르든 계속 한칸씩 당겨줘야되므로 여기서 en-=1
print(cnt)

#풀이시간 20분
# 메모리 32236kb 시간 148ms


# n = int(input())
# problem=input()
# case= ["B","R"]
# cur_color=problem[0]
# next_color=case[case.index(cur_color)-1]
# print(problem.count(cur_color+next_color)+1)



# 한번 짧게 풀어보았다...
# input()
# problem=input()
# check= "BR" if problem[0]=="B" else "RB"
# print(problem.count(check)+1)