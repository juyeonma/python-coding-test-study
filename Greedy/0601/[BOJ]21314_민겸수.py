# 참고 : https://velog.io/@qlql323/%EB%B0%B1%EC%A4%80-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-21314-%EB%AF%BC%EA%B2%B8%EC%88%98
# 규칙은 찾았지만.. 어떻게 구현할지 헷갈린 문제..
# 그냥 M을 최대한 모아 count를 세주었으면 되는 문제였다..!

s = input()

max_num = ''
min_num = ''
count = 0
for i in s:
    if i == 'M':
        count += 1
    else:
        if count:
            min_num += str((10 ** count)+5)
            max_num += str((10**count)*5)
        else:
            min_num += str(5)
            max_num += str(5)
        
        count = 0
if count > 0:
    min_num += str((10 ** (count-1)))
    max_num += '1' * count

print(max_num)
print(min_num)

# 다음에 다시 풀기!!