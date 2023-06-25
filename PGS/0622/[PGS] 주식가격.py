# prices의 길이가 최대 십만이라서 n^2을 하면 백억까지 나온다
# 그래서 2중 fop문을 돌리면 효율성에서 통과가 안될 거라고 생각했다.
# 다른 풀이를 생각하닥 못해서 답을 봤는데 그냥 n^2으로 풀리는 문제였다..
# 그래서 돌아와서 2중 for문으로 풀었다.
# 가격을 돌리면서 그 이후 가격에서 떨어지는 부분이 있는지 확인하는 것으로 로직은 간단하다


# 스택으로 푸는 O(n) 풀이가 있는데 이해가 안간다...
# 이게 정석인 풀이같다
# 2중for문 풀이는 테스트케이스가 추가되면 효율성테스트에서 틀릴 것 같다

def solution(prices):
    answer = []
    for i in range(len(prices)):
        temp=0
        for j in range(i+1, len(prices)):
            temp+=1
            if prices[i]>prices[j]:
                break
        answer.append(temp)
    return answer


# 스택풀이.. 이해시켜주세요
def solution(prices):
    length = len(prices)
    # 모든 가격 max값으로 세팅
    result = [ i for i in range (length - 1, -1, -1)]
    
    # 주식 가격이 떨어지는 경우를 찾아 수정
    stack = [0]
    for i in range (1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result