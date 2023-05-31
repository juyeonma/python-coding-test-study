# 깔끔하게 풀고 싶어서 고민하다가 시간이 오래 흘렀다.
# 결국 생각을 못하고 또 시간에 쫒겨 막 구현을 했다.
# 앞으로도 이런 고민을 하면서 계속 풀어봐야겠다

# B,R을 각각 왼쪽으로 밀었을 때와 오른쪽으로 밀었을 때를 나눠 구해서 최솟값을 구하면된다.
# 근데 이게 그리디인가? 문제 자체에서 최소를 구하라고 했으니 그리디라고 보는건가?..

input()
ball = input()
ball_l = ball[0] #맨 왼쪽의 색깔을 구하고 그 색깔에 맞는 색깔들을 이방향으로 밀거나 다른 색깔을 반대방향으로 밀기
ball_r = ball[-1] # 위와 같다
l_i=0
for i in range(len(ball)):  # 맨 왼쪽의 색을 구했을 때
    if ball[i]!=ball_l: # 한칸씩 이동하며 다른 색이 되었을때 인덱스를 구한다.
        l_i=i
        break

l_list=ball[l_i:] # 연속적인 왼쪽의 색을 제외하고 배열을 구한다.
r_i=0
for i in range(len(ball)-1,-1,-1):  # 오른쪽인 경우
    if ball[i]!=ball_r:
        r_i=i
        break

r_list=ball[0:r_i+1]  # 연속적인 오른쪽 색을 제외하고 배열을 구한다
print(min(l_list.count("R"),l_list.count("B"),r_list.count("R"),r_list.count("B"))) #각 경우에서의 색깔들의 개수를 구해서 최솟값을 출력

# 풀이시간 48분
# 메모리 32720kb 시간 136ms

# count메서드에서 순회를 한번씩 하니까 순회 횟수를 줄여보겠다고 for문 안에서 해결해봤는데 두 배 가까이 더 걸렸다.
# 순회가 줄어도 조건문으로 걸러지는 부분이 많아지면 더 오래걸리나보다
# input()
# ball = input()
# flag=False
# B_cnt=0
# R_cnt=0
# for i in range(len(ball)):
#     if ball[i]!=ball[0] and not flag:
#         flag=True
#     if flag:
#         if ball[i]=="B":
#           B_cnt+=1
#         else:
#           R_cnt+=1
# min_cnt=min(B_cnt,R_cnt)

# flag=False
# B_cnt=0
# R_cnt=0
# for i in range(len(ball)-1,-1,-1):
#     if ball[i]!=ball[-1] and not flag:
#         flag=True
#     if flag:
#         if ball[i]=="B":
#           B_cnt+=1
#         else:
#           R_cnt+=1

# print(min(min_cnt,R_cnt,B_cnt))
# 메모리 32236kb 시간 344ms

# 이런 풀이도  있었다.
# strip을 사용하면 빈칸 뿐만아니라 문자열도 벗겨낼수 있구나
# 처음에 풀면서 이걸 어떻게 생구현으로 구현해낼까 고민햇는데... 아는게 힘인 것 같다
# 또 의문인게 for문 사용하는 것보다 메서드 사용이 더 시간이 적게 드는 느낌도 있다.
# 아무래도 메서드는 함수안에서 이루어지는거리서 그런건가?
# 다른 로직이 없어서 시간이 짧을수도 있다
input()
ball = input()
rexplore=ball.rstrip(ball[-1])
lexplore=ball.lstrip(ball[0])
print(min(rexplore.count("R"),rexplore.count("B"),lexplore.count("B"),lexplore.count("R")))
# 메모리 32720kb 시간 52ms