def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1,len(prices)):
            if prices[j]>=prices[i]:
                cnt+=1
            else:
                cnt+=1
                break
        answer.append(cnt)
    return answer

x=[1, 2, 3, 2, 3]
print(solution(x))