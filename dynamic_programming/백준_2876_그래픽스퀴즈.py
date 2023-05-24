# 문제 이해가.. 잘 안된다ㅜ
n = int(input())
grade=[]
for i in range(n):
    grade.append(list(map(int, input().split())))

#퀴즈의 방식은 교수님이 수업이 시작할 때 어떤 두 책상을 선택하고, 
#두 책상과 그 사이에 있는 모든 책상에서 각각 한 명씩 지목해서 질문을 하고, 
#학생의 대답을 듣는 것이다.
d=[0]*6
for i in range(n):
    for j in range(2):
        d[grade[i][j]]+=1

print(d)
print(max(d),d.index(max(d)))