# 이 문제를 처음 봤을 때는 별 부분을 치환시켜서 풀면 될 것 같아서 정규식을 사용할 줄 알면 정말 좋겠다고 생각했습니다.
# 하지만 정규식을 잘 사용하지 못해서 다른 방식으로 풀었습니다.
# 문자열을 비교하면서 for문을 돌리다가 별을 만나면 별에 속해야할 문자열의 개수만큼 인덱스를 넘어가게 한 후
# 다시 별 이후의 문자열을 비교하도록 코드를 구성하였습니다.

# 다 풀고 틀려서 왜 그런가 했더니 패턴의 문자열이 입력되는 문자열의 길이보다 길어지는 경우를 생각하지 못해서 틀렸었습니다.
# 그래서 해당 코드는 따로 if문으로 처리하였습니다.
# 반례를 생각하는 능력이 중요하다

# 다른풀이
# 별을 기준으로 split을 하면 배열요소 두개가 생긴다 그러면 첫번째 요소의 문자열 길이만큼 앞에서부터 비교해보고 두번째요소의 요소 길이만큼 뒤에서부터 비교해봐서 같으면 답 다르면 오답
# 이 방식은 자바스크립트를 사용할때 종종 사용했던 방식인데 왜이거 풀땐 생각이안났을까?
# split에 대한 관점을 바꿔보는게 좋을 것같다. split을 단순히 나눈다라고 생각하지말고 다르게 생각해보면 이것을 통해 길이 비교도 가능하다
# js에서는 문자열 안에 찾고 싶은 문자열의 개수를 구할 때 split을 통해 구할 수 있었는데, 파이썬은 count가 있구나.. 굉장하다..
# 이런류의 문제가 종종나오고 프로그래머스에도 해당 관련 문제가 있으니까 나중에 풀어보자

# 메서드에 대한 이해도를 더 높이기

# 31256kb 52ms 
# 다른풀이 : 31256kb 56ms
# 유의미한 차이는 없다.

N =int(input())
pattern = input()
patternAlphabetNum = len(pattern)-1   # 패턴 문자열에서 알파벳의 개수

for _ in range(N):
    s = input()
    starCount=len(s)-patternAlphabetNum     # 별에 치환 될 문자열 개수 = 판단해야 할 문자열 - (len(패턴문자열)-1)
    s_i=0
    if patternAlphabetNum>len(s):
        print("NE")
        continue
    for i in range(len(pattern)):
        if pattern[i]==s[s_i]:
            pass
        elif pattern[i]=="*":
            s_i=i+starCount-1
        else:
            print("NE")
            break
        s_i+=1
    else:
        print("DA")


# 다른풀이
# N =int(input())
# pattern = input().split("*")
# first = pattern[0]
# second = pattern[1]
# for _ in range(N):
#     s = input()
#     if s[:len(first)] == first and s[-len(second):] == second and len("".join(pattern)) <= len(s):
#         print("DA")
#     else:
#         print("NE")