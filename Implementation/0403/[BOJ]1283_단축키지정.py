n = int(input())
option = []

for _ in range(n):
    s = list(input().split())
    for i in range(len(s)):
        if s[i][0].lower() not in option:
            option.append(s[i][0].lower())
            s[i] = '['+s[i][0]+']' + s[i][1:]
            print(' '.join(s))
            break
    else:
        for j in range(len(s)):
            flag = False
            for k in range(len(s[j])):
                if s[j][k].lower() not in option:
                    option.append(s[j][k].lower())
                    flag = True
                    s[j] = s[j][:k] + '['+s[j][k]+']' + s[j][k+1:]
                    print(' '.join(s))
                    break
            if flag:
                break
        else:
            print(*s)
# true, false랑 for문 순서는 다 맞았는데
# 바로 출력하고자 해서 실패한 것 같다!
# 단어[번호] 안에 []와 함께 저장해서 출력하면 되었던 문제..!
# https://fre2-dom.tistory.com/403 님꺼 참고해서 고침
