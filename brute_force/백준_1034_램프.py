'''
# 백준_1034_램프. 골드 4. 풀이: 23.05.07 실패 -> 23.05.08 성공

# 풀이방법
## 두번째 시도: 성공
- 스터디원의 풀이를 참고하여, 다시 반례를 살펴보았다.
    - 실패한 풀이에서는 cnt = i.count('0') 일 때, k % m == cnt % 2를 체크했다.
    - 왜그랬는지 모르겠지만.. 이때는 나머지가 1과 0으로만 나온다고 생각했다. 즉 2로 나누는 것과 혼동했다.
    - 따라서 이번에는 k % 2 == cnt % 2 을 체크할 것이다.
    
## 첫번째 시도: 실패한 풀이방법
- 꺼져있는 불은 홀수번 눌러야 켜진다. 즉 0 -> 누른다 -> 1로 변한다.
- 켜야할 열의 개수가 짝수인지 홀수인지 구하고, 그에 따른 패턴들을 list로 구한다.
- 딕셔너리로 입력되는 행을 패턴 list에서 찾아 갯수를 센다.
- 가장 많은 갯수를 출력.

홀수=짝수+홀수
짝수=홀수+홀수, 짝수+짝수

- 예
3열, 6버튼: 6 % 3 = 0 -> 켜야할 열의 개수: 짝수개
111, 001, 010, 100

4열 5버튼: 5 % 4 = 1 -> 켜야할 열의 개수: 홀수개
0111, 1011, 1101, 1110, 0001, 0010, 0100, 0100


# 반례
1 1
0
1
답 : 1

1 1
1
0
답 : 1

3 3
000
000
001
1
답 : 0
'''

'''
# 보완할 것
- 나머지를 이용한 짝수 홀수 판단을 왜 k % m로 하는 실수를 저질렀을까ㅠㅠ 민망쓰..
- 동일 패턴을 다시 계산하는 수고를 줄이기 위해서 pattern 리스트에 있는 원소인지 판단하는 코드를 추가해봤지만, 시간 차이가 없었다.
- 그렇지만 나중에 복잡한 코드에서는 효과가 있을지도..?

'''
# 두번째 시도: 성공한 풀이
import sys
input = sys.stdin.readline

# 행, 열
n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
k = int(input())

answer = 0
for i in arr:
    cnt = i.count('0')
    if cnt <= k and cnt % 2 == k % 2:
        answer = max(answer, arr.count(i))
print(answer)
'''
빠른 코드지만, 동일 패턴을 계속 만나게 된다.
즉, count -> if -> answer 최댓값 갱신 하는 수고가 반복된다.

그래서 패턴 리스트에 들어있다면 통과, 조건에 맞는 패턴은 리스트에 추가하는 방법을 써봤다.

pattern = []
for i in arr:
    if i in pattern:
        continue
    cnt = i.count('0')
    if cnt <= k and cnt % 2 == k % 2:
        pattern.append(i)
        answer = max(answer, arr.count(i))
        
그러나.. 이미 충분히 빠른 코드라서, 더이상의 시간 단축은 이루어지지 않았다.
'''

'''
# 아예 패턴을 먼저 구하는 방법 -> 시간 초과 혹은 메모리 초과ㅠㅠ
all_patterns = [bin(i)[2:].zfill(m) for i in range(2**m) ]
answer = 0
for i in all_patterns:
    cnt = i.count('0')
    if cnt <= k and cnt % 2 == k % 2:
        answer = max(answer, arr.count(i))
'''


# 첫번째 시도: 실패한 풀이
# 행, 열
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
k = int(input())

# 누를 버튼이 없을 때
if k == 0:
    cnt = 0
    for i in arr:
        if '0' in i:
            continue
        cnt += 1
    print(cnt)
    
# 1열, 1버튼일 때
elif m == 1 and k == 1:
    print(arr.count('0'))
    
else:
    check = 0 if k % m == 0 else 1

    dic = {}
        
    for i in arr:
        cnt = i.count('0')
        
        if i in dic:
            dic[i] += 1
                
        elif cnt <= k and cnt % 2 == check:
            dic[i] = 1
            
    if dic:
        print(max(dic.values()))
    else:
        print(0)

'''
# 결과
메모리: 31256 KB
시간: 40 ms
코드 길이: 276 B
'''