def solution(msg):
    answer = []
    dict = {}
    a = ord("A")
    for i in range(26):
        dict[chr(a + i)] = i + 1

    i = 0
    msg = list(msg)
    while msg:
        temp = msg[0]
        new = temp
        for i in range(1, len(msg)):
            new += msg[i]
            if new not in dict:
                dict[new] = len(dict) + 1
                break
            else:
                temp += msg[i]
        answer.append(dict.get(temp))
        for i in range(len(temp)):
            msg.pop(0)

    return answer


# 다른 사람의 코드
# 느낀점 : zip 진짜 중요하군..
# 슬라이싱을 활용을 많이 했다는 것을 알았다
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k: v for (k, v) in zip(alphabet, list(range(1, 27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg) + 1):
            if msg[0:i] not in d:
                answer.append(d[msg[0 : i - 1]])
                d[msg[0:i]] = len(d) + 1
                msg = msg[i - 1 :]
                break

    return answer


solution("KAKAO")
