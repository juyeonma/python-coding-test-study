# 3x3행렬 부분 행렬만 뒤집는다는 것을 보지 못하고 처음에 엄청 헤맸다. 
# 왜 자꾸 문제를 똑바로 읽지 않는지 모르겠다...
# 포스트잇에 써두고 알고리즘 문제 풀기 전에 읽고 풀어야되겠다..
# 그리고 로직을 완성한 후에도 계속 틀렸는데 나는 3x3행렬로 바꿀수 없으면 -1로 출력하는걸 3x3행렬이 되지 않으면 -1이 되는 것으로 착각하고 자꾸 틀렸다.
# 코딩테스트였다면 이미 히든케이스에서 걸러졌을 것 같다. 이 부분이 걱정이 되는데 일단 내가 할 수 있는건 문제를 똑바로 읽는 것이므로 이것부터 고쳐야겠다.

# 3x3 부분행렬로 뒤집을 수 있는지를 묻는 것이고 N이 50으로 작으므로 행렬을 두번 돌아도 시간이 넉넉하다.
# O(N^2 * 9)정도로 풀어서 한번 행렬 돈 것으로 풀었다.
# 처음 위치부터 돌면서 다르면 뒤집고 같으면 넘어가는 방식으로 풀었다. 해당 위치에서 a,b가 다르다면 무조건 뒤집어야 마지막 인덱스에서 같은지 다른지를 판단 할 수 있기 때문이다.

n,m=map(int,input().split())

def matrix(n,m):
    a=[list(input()) for _ in range(n)]
    b=[list(input()) for _ in range(n)]
    cnt=0
    if n<3 or m<3:    # n과 m 중 하나가 3미만이라면 행렬을 바꿀 수 없으므로 바로 비교를 한다.
        for i in range(n):
            for j in range(m):
                if a[i][j]!=b[i][j]:  #하나라도 다르면 -1 출력
                    print(-1)
                    return
        else:
            print(0)  # 모두 같으면 0
            return
    for i in range(n-2): # 부분행렬 3x3 전환이 가능하게 하려면 범위는 n-2까지
        for j in range(m-2):
            if a[i][j]!=b[i][j]:   # 다른 부분이 있다면 3x3부분행렬만큼 돌면서 전환을 해준다
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        a[k][l]="1" if a[k][l]=="0" else "0"
                cnt+=1  # 다를경우 바꿔주기 때문에 카운팅

    for i in range(n):  # 마지막으로 두 행렬을 비교한다.
        for j in range(m):
            if a[i][j]!=b[i][j]:  # 하나라도 다르면 -1 출력하고 종료
                print(-1)
                return
    else:   # 모두 같으면 연산 횟수 출력
        print(cnt)

matrix(n,m)
            
#메모리 31256KB 시간 48ms
#풀이시간 35분?  이십분대에 로직은 다 짰는데 자꾸 틀려서 반례를 보고 맞췄습니다...



# n,m=map(int,input().split())

# def matrix(n,m):
#     a=[list(input()) for _ in range(n)]
#     b=[list(input()) for _ in range(n)]
#     cnt=0

#     def check(n,m):
#       for i in range(n):
#           for j in range(m):
#               if a[i][j]!=b[i][j]:
#                   print(-1)
#                   return
#       else:
#           print(cnt)

#     def convert(i,j):
#         for k in range(i,i+3):
#             for l in range(j,j+3):
#                 a[k][l]="1" if a[k][l]=="0" else "0"

#     if n<3 or m<3:
#         check(n,m)
#         return
    
#     for i in range(n-2):
#         for j in range(m-2):
#             if a[i][j]!=b[i][j]:
#                 convert(i,j)
#                 cnt+=1
#     check(n,m)

# matrix(n,m)

