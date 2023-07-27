# # k가 5보다 작으면 0
# # 단어들 전부 중복제거한 후 k보다 작으면 못만듦
# # k-5 < 단어의 수 빼기
# # k-5개 채운 후 다 확인하면서 추가안되는 단어만 계속 카운팅
# import sys

# n,k = map(int,input().split())
# words = []
# alphabet = set()
# max_word = 0
# for _ in range(n):
#     needed_word=list(set(input())-set(["a","n","t","i","c"]))
#     if len(needed_word)<=k-5:
#         words.append(needed_word)
# k-=5
# vis = [0]*len(words)
# def dfs(x,alphabet,count):
#     global max_word
#     if x==len(words):
#         max_word = max(max_word,count)
#         if max_word==len(words):
#             print(max_word)
#             sys.exit()

#     for i in range(x,len(words)):
#         if not vis[i]:
#             vis[i]=1
#             temp=set(words[i])|alphabet
#             if len(temp)<=k:
#                 dfs(i+1,temp,count+1)
#             else:
#                 dfs(i+1,alphabet,count)
#             vis[i]=0

# dfs(0,alphabet,0)
# print(max_word)


# k가 5보다 작으면 0
# 단어들 전부 중복제거한 후 k보다 작으면 못만듦
# k-5 < 단어의 수 빼기
# k-5개 채운 후 다 확인하면서 추가안되는 단어만 계속 카운팅
import sys
n,k = map(int,input().split())

if k < 5:
    print(0)
    sys.exit()
elif k == 26:
    print(n)
    sys.exit()

words = []
for _ in range(n):
    word = set(sys.stdin.readline().rstrip())
    if len(word) >=5:
        words.append(word)

alphabet = [0]*26
answer = 0
for w in ("a","c","i","n","t"):
    alphabet[ord(w)-ord("a")]=1

def dfs(idx,cnt):
    global answer
    if cnt==k-5:
        temp_cnt=0
        for word in words:
            check=True
            for w in word:
                if not alphabet[ord(w)-ord("a")]:
                    check=False
                    break
            if check:
                temp_cnt+=1
        answer = max(answer,temp_cnt)
        return
    
    for i in range(idx,26):
        if not alphabet[i]:
            alphabet[i]=True
            dfs(i,cnt+1)
            alphabet[i]=False

dfs(0,0)
print(answer)
