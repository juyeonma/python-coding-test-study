<<<<<<< HEAD
n, m = tuple(map(int, input().split()))
lamp = []
for _ in range(n):
    lamp.append(input())
k = int(input())

cnt = 0

for j in range(n):
    zero = 0
    for num in lamp[j]:
        if num=='0':
            zero+=1 #행별로 0의 개수 구하기
    light=0 #현재 행과 같은 값을 가진 행 개수 세기
    if zero<=k and zero%2==k%2: #0의 개수가 스위치를 누르는 횟수보다 작거나 같아야됨, 또는 나머지의 수가 같아야함
        for i in range(n):
            if lamp[i]==lamp[j]:
                light+=1
    cnt = max(cnt, light) #가장 많은 수를 저장
print(cnt)

#코드길이 : 532B
#시간 : 44ms
=======
'''
# 백준_1034_램프. 골드 4. 풀이: 23.05.07 -> 실패

# 풀이방법
- 꺼져있는 불은 홀수번 눌러야 켜진다. 즉 0 -> 누른다 -> 1로 변한다.
- 켜야할 열의 개수가 짝수인지 홀수인지 구하고, 그에 따른 패턴들을 list로 구한다.
- 딕셔너리로 입력되는 행을 패턴 list에서 찾아 갯수를 센다.
- 가장 많은 갯수를 출력.
    
홀수=짝수+홀수
짝수=홀수+홀수, 짝수+짝수

# 예
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
- 쉽다고 생각했는데, 0버튼이거나 1열 1버튼일 경우를 생각못해서 추가했다. 그런데도 9%에서 틀림..
- 도저히 반례가 생각나지 않는다ㅠㅠ
'''

# 풀이 기록
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
메모리:  KB
시간:  ms
코드 길이:  B
'''
>>>>>>> 02082bab0c862eac8ef77bd15cb7a0be31497c1c
