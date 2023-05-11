import sys
input=sys.stdin.readline
n = int(input())
m = int(input())

break_button=list(map(int, input().split()))

cnt=abs(100-n) #-,+만 눌러서 n에 도달할때까지의 개수(최솟값을 구해야하니까 최대값을 먼저 구함)

for i in range(1000001): #채널 자체가 무한대,, 
    i = str(i) #채널을 각 자리수로 분류(숫자 한자씩 누르니까)
    for j in range(len(i)):
        if int(i[j]) in break_button: #고장난 숫자를 눌러야된다면 종료
            break
        elif j == len(i)-1: #채널의 마지막 자리수까지 갔다면
            cnt=min(cnt,abs(int(i)-n)+len(i)) #번호를 누른 횟수+n까지의 차이
print(cnt)

#코드길이 : 651 B
#시간 : 3384ms