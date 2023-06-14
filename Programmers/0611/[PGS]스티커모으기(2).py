def solution(sticker):
    answer = 0

    total = sum(sticker)
    num = 0
    for i in range(1, len(sticker), 2):
            num += sticker[i]
    if len(sticker) == 1:
        answer = total
    elif len(sticker) % 2 == 0:
        answer = max(total-num, num)
    else:
        answer = max(total-num-sticker[0], num, total-num-sticker[-1])
    return answer

print(solution([5, 1, 16, 17, 16]))

# 반례가 뭘까?..
# 최댓값이니깐.. 반례가 당연히 존재하는 문제였다..
# dp로 전에 백준의 스티커문제랑 비슷한 느낌의 문제인 것 같다.

def solution(sticker):
    if len(sticker)==1:
        return sticker[0]
    
    dp1 = [0 for _ in range(len(sticker))]  # use first sticker
    dp2 = [0 for _ in range(len(sticker))]  # unuse first sticker
    
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    
    dp2[1] = sticker[1]
    
    for i in range(2,len(sticker)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
    for i in range(2,len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
    
    return max(max(dp1),max(dp2))

# 문제만 보니깐.. 유형이 바로 생각나지않았다..ㅠㅠ..