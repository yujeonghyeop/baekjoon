s = input()
cnt=[]
check=True
strcnt=''
answer=''
for i in range(len(s)):
    if s[i]=='<':
        if len(strcnt)!=0:
            strcnt=strcnt[::-1]
            answer+=strcnt
            strcnt=''
        check=False
        strcnt+=s[i]
    elif s[i]=='>':
        strcnt+=s[i]
        answer+=strcnt
        strcnt=''
        check=True
    elif check==False:
        strcnt+=s[i]
    elif s[i]==' ':
        strcnt=strcnt[::-1]
        answer=answer+strcnt+' '
        strcnt=''
    else:
        strcnt+=s[i]
if len(strcnt)!=0:
    strcnt = strcnt[::-1]
    answer+=strcnt
print(answer)

