'''
# 백준_9996_한국이 그리울 땐 서버에 접속하지. 실버 3. 풀이: 23.05.03

# 풀이방법
- 패턴은 소문자 여러 개와 * 하나.
    - *는 앞, 중간, 뒤 세곳에 올 수 있음.
    - *을 기준으로 패턴을 나누면, list의 길이는 1개 또는 2개.

예.
*bcd
a*cd
ab*d
abc*

# 풀이
- 방법 1. 구분자(*)의 위치별로 나누어서 비교
- 방법 2. 굳이 구분자 위치를 알 필요 없이, 처음부터 구분자 기준으로 split 하여 비교.

# 반례
- 입력
1
AB*BD
ABD

- 출력
NE
'''

'''
# 보완할 것
- 여기서는 입력이 매우 작아서 시간차이가 안났지만, 바로 split 해서 비교하는걸 까먹지 말자.
- index가 필요하다면 s.find('*')를 까먹지 말자.
- startswith과 endswith이 그냥 index로 slicing 후 비교하는거랑 속도 차이가 얼마나 날까?
'''

# 방법 1. 풀이 기록
n = int(input())
p = input()
p2 = p.split('*')

len_p2 = len(p) - 1
split_place = 0

for _ in range(n):
    word = input()
    
    if len(word) < len_p2:
        print('NE')
        
    elif p[0] == '*':
        if word[-len(p2[0]):] == p2[0]:
            print('DA')
        else:
            print('NE')
            
    elif p[-1] == '*':
        if word[:len(p2[0])-1] == p2[0]:
            print('DA')
        else:
            print('NE')
            
    else:
        if word[:len(p)-len(p2[1])-1] == p2[0] and word[-len(p2[1]):] == p2[1]:
            print('DA')
        else:
            print('NE')


# 방법 2. 풀이 기록            
n = int(input())

'''
바로 split 해도 되고, index가 필요하다면 find -> slicing 해도 된다.
idx = input().find('*')
first, last = p[:idx], p[idx+1:]
'''

first, last = input().split('*')
len_p = len(first) + len(last)
        
for _ in range(n):
    word = input()

    # word[:len(first)+1] == first and word[-len(last):] == last 와 같다.
    if len(word) >= len_p and word.startswith(first) and word.endswith(last):
        print('DA')
        
    else:
        print('NE')
'''
# 결과
메모리: 31256 KB
시간: 48 ms
코드 길이: 319 B
'''