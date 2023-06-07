# 문제를 어떻게 풀면 좋을까 싶어서
# 현재 예제말고 다른 예제를 넣어봄
# 3 - 6 - 1 - 4
#   3   5   2
# 3 x (3 + 5) + 1 x 2 가 닶
# => 작은 값이 바뀌면 작은 값을 대입해서 total 을 구해주면 됨

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

total = 0
min_value = city[0]
i = 1
while road:
    if min_value <= city[i]:
        total += min_value * road[0]
    else:
        total += min_value * road[0]
        min_value = city[i]
    i += 1
    del road[0]
print(total)
# print(total)
# 메모리 : 46076KB 시간 : 1928ms
# 왜 시간이 오래 걸렸을까? while문을 사용했기 때문?! => for문으로 변경해봄

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

total = 0
min_value = city[0]
for i in range(1, n):
    if min_value <= city[i]:
        total += min_value * road[0]
    else:
        total += min_value * road[0]
        min_value = city[i]
    del road[0]
print(total)
# 시간 100ms정도 줄었음.. 1892ms
# 더 줄이기 위해서 중복된 줄인 total을 빼주고 del road도 없애주기
n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

total = 0
min_value = city[0]
for i in range(1, n):
    total += min_value * road[i-1]
    if min_value > city[i]:
        min_value = city[i]
print(total)

# 시간 => 116ms 훨씬 줄었다..!
# del road[0]이 시간이 오래 걸렸다 
# => 따로 해보았는데 del road[0]를 없애고 road[i-1]로 대체하는게 훨씬 빨랐다.
# del 사용 최대한 안하기로..!
# del 왜 시간이 많이?? => 뇌피셜이지만, del 함수를 사용함으로써 for문 안에서 또 시간 복잡도 O(n)만큼 증가하기 때문에인것 같다..!
# for문만 사용 => O(n) for문 + del문 => O(n^2) ?!가 되기 때문이 아닐까..