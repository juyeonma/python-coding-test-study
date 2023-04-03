n = int(input())

dic=[]

for _ in range(n):
    word=list(map(str, input().split()))
    
    for i in range(len(word)):
        if word[i][0].upper() not in dic:
            dic.append(word[i][0])
            word[i]="["+word[i][0]+"]"+word[i][1:]
            print(" ".join(word))
            break
    else:
        for j in range(len(word)):
            flag=False
            for k in range(len(word[j])):
                if word[j][k].upper() not in dic:
                    dic.append(word[j][k].upper())
                    flag=True
                    word[j] = word[j][:k]+"["+word[j][k]+"]"+word[j][k+1:]
                    print(" ".join(word))
                    break
            if flag:
                break
        else:
            print(*word)