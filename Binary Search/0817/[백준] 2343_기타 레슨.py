# 크기가 17일 때 cnt는 4가 된다 원래는 3이 되어야 하는데 4로 나오게 하고 풀면 답이 나온다
# 왜 이런걸까? 이 부분을 어떻게 해결할지 감이 안잡혀서 그냥 답을 봤더니 생각했던 논리는 같은데 4로 나오는 부분을 어떻게 수정할 지 생각했지만
# 그냥 4로 해도 답이 나온다.. 뭐지..

n,m = map(int,input().split())
lectures = list(map(int,input().split()))

def check_size(mid):
    s=0
    cnt=1
    for i in range(n):
      if s+lectures[i]>mid:
        cnt+=1
        s=0
      s+=lectures[i]
    if cnt>m:
      return False
    else:
      return True

def binary_search():
    st=max(lectures)
    en=sum(lectures)
    while st<=en:
      mid=(st+en)//2
      status=check_size(mid)
      if status:
        en=mid-1
      else:
        st=mid+1
    return st

print(binary_search())