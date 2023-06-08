# 첫번째 풀이는 기준을  hash값에 둔것이고 두번째 풀이는 기준을 검사해야할 번호로 두었다.
# 두번째 풀이는 검색햇을 때 나오는 방식인데 더 깔끔하고 정석인 풀이인 것 같다.
# 첫번째 풀이는 모든 경우를 다 set에 넣어두고 풀지만, 두 번째 풀이는 전화번호의 가지수만 넣어두고 그 때 그 때 확인하는 방식이라서 시간이 더 짧고 깔끔한 것 같다

#길이가 1인 부분부터 n-1까지 돌리는 이유는 n을 넣을경우 그 아래 for문에서 확인하기 복잡해지고, 같은 전화번호가 존재하지 않기 때문에 같은 길이라면 무조건 접두어가 될 수 없고, 다른길이라면 n의길이만큼 확인할 필요가 없으므로  n-1까지로 해도 논리적으로 문제가 없다.

def solution(phone_book):
    answer = True
    check=set()
    for s in phone_book: # 모든 전화번호 경우의 수를 돌면서
        for i in range(1,len(s)): # 길이가 1인 부분부터 n-1까지 돌리면서 set에 추가.
            check.add(s[0:i])
    for s in phone_book: #확인하기 위해서 전활번호를 돌리면서
        if s in check:  # 그 전화번호가 set에 있는지 확인한다
            answer=False 
            break       
    else:
        return answer
    return answer

#걸린시간 19분

# 테스트 1 〉	통과 (25.28ms, 17.5MB)
# 테스트 2 〉	통과 (23.89ms, 17.5MB)
# 테스트 3 〉	통과 (613.35ms, 31.2MB)
# 테스트 4 〉	통과 (1109.72ms, 244MB)


# def solution(phone_book):
#     answer = True
#     hash_map = {}
    
#     for number in phone_book:
#         hash_map[number] = 1 # 해시에 모든 전화번호를 넣는다.
    
#     for number in phone_book: # 전화번호를 돌면서
#         temp=""
#         for num in number:  #해당 전화번호의 앞자리부터 한자리씩 추가하면서 그 전화번호가 hash에 있는지 확인한다
#             temp+=num
#             if temp in hash_map and temp!=number:
#                 answer=False
#                 return answer
#     return answer

# 테스트 1 〉	통과 (1.18ms, 11.3MB)
# 테스트 2 〉	통과 (1.15ms, 11.3MB)
# 테스트 3 〉	통과 (474.92ms, 46.7MB)
# 테스트 4 〉	통과 (206.84ms, 34.5MB)

# set으로 하면 길이가 커질수록 더 효율적인 것처럼 보인다. 이유는 모르겠다. 하지만 근소한 차이이다
# def solution(phone_book):
#     answer = True
#     number_set=set()
    
#     for number in phone_book:
#         number_set.add(number)
    
#     for number in phone_book:
#         temp=""
#         for num in number:
#             temp+=num
#             if temp in number_set and temp!=number:
#                 answer=False
#                 return answer
#     return answer

# 테스트 1 〉	통과 (1.39ms, 11.4MB)
# 테스트 2 〉	통과 (1.38ms, 11.3MB)
# 테스트 3 〉	통과 (442.47ms, 41.4MB)
# 테스트 4 〉	통과 (172.05ms, 39.1MB)

# 아이디어 풀이법
# 출제의도에는 벗어났지만 이런 아이디어 배워두면 그리디쪽에서 도움을 받을 수 있을 것 같은 느낌
# sort를 하면 숫자가 빠른순으로 정렬된다.
# 우리가 비교해야할 것은 접두어이고 접두어를 가지기만 하면 false를 반환하면 되므로 해당 위치의 숫자와 다음 위치의 숫자만 비교하면 된다.
# 정렬되어있으므로 가장비슷한 문자열이 가장 가까이 위치한다는 점과 접두어가 존재하는 하나의 경우만 구하면 된다는 점에 의해 가능한 아이디어이다 

# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
#             return False
#     return True

# 테스트 1 〉	통과 (2.75ms, 10.8MB)
# 테스트 2 〉	통과 (2.81ms, 10.9MB)
# 테스트 3 〉	통과 (109.60ms, 30.8MB)
# 테스트 4 〉	통과 (90.42ms, 28.1MB)