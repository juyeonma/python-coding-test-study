# 1로 끝나는건 2로 나눌 수 없음 => 무조건 1 없애주기
# 1로 끝나지 않는건 다 2로 나눔 => 2로 나누어지지 않는다면 -1
import sys
a, b = map(int, input().split())

count = 0
while b > 1: # b > a로 하면 더 시간 단축 가능
    if str(b)[-1] == '1': # b % 10 == 1로 하면 더 간단하게 가능..
        b = int(str(b)[:len(str(b))-1])
    else:
        if b % 2 == 0:
            b //= 2
        else:
            break
    count += 1
    if b == a:
        print(count+1)
        sys.exit(0)
print(-1)

# 메모리 : 31256KB 시간 : 40ms