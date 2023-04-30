N = int(input())
possibleList = []
for _ in range(N):
    possibleList.append(input().split())

number = 123
cnt = 0
while number <= 987:
    number = str(number)
    numberSet = set(number)
    for num, strike, ball in possibleList:
        strike = int(strike)
        ball = int(ball)
        st = 0
        ba = 0
        for i in range(len(num)):
            if num[i] in numberSet:
                if num[i] == number[i]:
                    st += 1
                else:
                    ba += 1
        if st != strike or ba != ball:
            break
    else:
        cnt += 1
    number = int(number)
    number += 1
    while len(set(str(number))) != 3 or "0" in set(str(number)):
        number += 1
print(cnt)