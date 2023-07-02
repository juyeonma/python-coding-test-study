# 처음엔 짝수의 경우와 홀수의 경우를 나누어서 구할까 했었다.
# 그런데 너무 복잡하다는 생각이 들었고, 홀수인 알파벳은 한 종류를 넘어가게 되면 팰린드롬은 불가능하다
# 그래서 이 경우에 대해서 for문을 돌리며 확인하고 for문을 return 반환없이 넘어가면
# 하나만 홀수이거나 전부 짝수라는 소리이다.
# 그렇다는 건 모두 펠린드롬이 가능하다는 것이므로 개수 나누기 2를 해서 앞 부분을 구하고 홀수가 있었다면
# 저장된 알파벳을 더하고 뒷부분을 뒤집어서 구하면 된다.


# 처음엔 첫번째 풀이처럼 풀었고, 그 다음엔 굳이 for문을 두번 쓸 필요 없이 정렬된 for문을 돌리면서
# 홀수의 개수가 몇 개인든 상관없이 그냥 갱신한다
# 그리고 첫번째 풀이처럼 완성된 문자열을 구하고, 홀수가 여러개였다면 새로운 홀수 알파벳이 mid에 들어가므로
# 원래 문자열과 새로운 문자열의 길이가 달라진다
# 다르면 한수를 출력하고 같으면 새로운 문자열을 출력하면 된다.


from collections import defaultdict

def func():
    s = input()
    alphabet = defaultdict(int)
    for v in s:
        alphabet[v]+=1
    
    cnt=0
    temp=""
    for v in alphabet:
        if alphabet[v]%2==1:
            cnt+=1
            temp=v
        if cnt>1:
            print("I'm Sorry Hansoo")
            return
    
    sorted_alphabet=sorted(alphabet.items())
    new_s = ""
    
    for (v,i) in sorted_alphabet:
        new_s+=v*(i//2)

    reverse_new_s = new_s[::-1]
    if temp:
        new_s+=temp

    new_s+=reverse_new_s
    print(new_s)

func()




# 수정
from collections import defaultdict

def func():
    s = input()
    alphabet = defaultdict(int)
    for v in s:
        alphabet[v]+=1

    sorted_alphabet=sorted(alphabet.items())
    mid = ""
    new_s=""
    for (v,i) in sorted_alphabet:
        new_s+=v*(i//2)
        if i%2==1:
            mid=v
    new_s += mid + new_s[::-1]

    if len(s)!=len(new_s):
        print("I'm Sorry Hansoo")
    else:
        print(new_s)

func()


# 메모리 : 34244kb 시간 : 64ms
# 걸린시간 :30분이상?