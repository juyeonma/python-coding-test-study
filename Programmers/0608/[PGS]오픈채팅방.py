# 풀이가 바로 생각났던 문제...
# 이런 문제만 나왔으면 좋겠다..
def solution(record):
    answer = []
    total_comment = []
    total = {}
    while record:
        comment = record.pop(0).split()
        if comment[0] == "Enter":
            total_comment.append([comment[1], comment[0]])
            total[comment[1]] = comment[2]
        elif comment[0] == "Leave":
            total_comment.append([comment[1], comment[0]])
        else:
            total[comment[1]] = comment[2]
    for id, comment in total_comment:
        if comment == "Enter":
            answer.append(total.get(id) + "님이 들어왔습니다.")
        else:
            answer.append(total.get(id) + "님이 나갔습니다.")
    return answer


# solution(
#     [
#         "Enter uid1234 Muzi",
#         "Enter uid4567 Prodo",
#         "Leave uid1234",
#         "Enter uid1234 Prodo",
#         "Change uid4567 Ryan",
#     ]
# )
