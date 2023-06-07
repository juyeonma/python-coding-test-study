# 첫 번째 풀이
# 채점 결과
# 정확성: 66.7
# 효율성: 8.3
# 합계: 75.0 / 100.0
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i == j:
                continue
            else:
                if phone_book[j].count(phone_book[i]) > 0:
                    answer = False
            if not answer:
                break
    return answer


# 반례와 시간 효율성 생각해보기
# 반례는?
# 접두어여야 함 => 즉, 앞에 포함되었어야 했다..! 그렇기 때문에 count는 적절하지 않음


# 두 번째 풀이
# 채점 결과
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][: len(phone_book[i])]:
                answer = False
                break
        if not answer:
            break
    return answer


# 시간은 어떻게 줄이면 좋을까..?
# 딕셔너리 사용..!
# 채점 결과
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    dict = {}
    for i in range(len(phone_book)):
        dict[phone_book[i]] = 1
        for j in range(i + 1, len(phone_book)):
            if phone_book[j][: len(phone_book[i])] in dict:
                answer = False
                break
        if not answer:
            break
    return answer


# 여전히 효율성이 높아지지 않았다.. 다른 사람의 풀이를 참고해서 풀어보기
def solution(phone_book):
    # phone_book.sort(key=lambda x: len(x))
    dict = {}
    for i in phone_book:
        dict[i] = 1
    for i in phone_book:
        temp = ""
        for n in i:
            temp += n
            if temp in dict and temp != i:
                return False
    return True


# 다른 사람의 풀이
# 느낀 점 : zip의 활용, startswith 함수.., return 사용
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# 해시를 이용한 정석 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
