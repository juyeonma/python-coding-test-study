n = int(input())
dic=[]

for _ in range(n):
    word=list(map(str,input().split())) #공백을 기준으로 먼저 나눔
        
    for i in range(len(word)):
        if word[i][0].upper() not in dic: #맨 앞글자가 사전에 없으면
            dic.append(word[i][0].upper()) #추가
            word[i]="["+word[i][0]+"]"+word[i][1:] #출력 조건
            print(" ".join(word))
            break
    #앞에 for문에서 break되지 않았으면(앞글자가 사전에 있으면)
    else:
        for j in range(len(word)): #단어 탐색
            flag=False #사전에 있는지 없는지 확인
            for k in range(len(word[j])):
                if word[j][k].upper() not in dic: #해당 단어를 대문자로 바꾸었을때 사전에 없으면
                    dic.append(word[j][k].upper()) #추가(대문자로 바꿔야함)
                    flag=True #사전에 있음을 확인
                    word[j]=word[j][:k] + "[" +word[j][k] + "]"+ word[j][k+1:]
                    print(" ".join(word))
                    break
            if flag:#사전에 담았으니까 break
                break
        else:#단축키를 설정할 수 없으므로 그대로 출력
            print(*word)
