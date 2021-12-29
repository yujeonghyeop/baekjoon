import sys
a = sys.stdin.readline()
cntalpha=''
cnt=[]
check=True
for i in range(len(a)-1):
    if a[i].isalpha():
        cntalpha+=a[i]
    else:
        if a[i]=='(':
            cnt.append(a[i])
        elif a[i]==')':
            while(True):
                print(cnt)
                cnt1=cnt.pop()
                if cnt1=='(':
                    break
                else:
                    cntalpha+=cnt1
        elif a[i]=='*':
            if len(cnt)==0:
                cnt.append(a[i])
            else:
                for k in range(len(cnt)):
                    if cnt[-1]=='(' or cnt[-1]=='+' or cnt[-1]=='-':
                        break
                    else:
                        cntalpha+=cnt.pop()
                cnt.append(a[i])
        elif a[i]=='/':
            if len(cnt)==0:
                cnt.append(a[i])
            else:
                for k in range(len(cnt)):
                    if cnt[-1]=='(' or cnt[-1]=='+' or cnt[-1]=='-':
                        break
                    else:
                        cntalpha+=cnt.pop()
                cnt.append(a[i])
        elif a[i]=='+':
            if len(cnt)==0:
                cnt.append(a[i])
            else:
                for k in range(len(cnt)):
                    if cnt[-1]=='(':
                        break
                    else:
                        cntalpha+=cnt.pop()
                cnt.append(a[i])    
        elif a[i]=='-':
            if len(cnt)==0:
                cnt.append(a[i])
            else:
                for k in range(len(cnt)):
                    if cnt[-1]=='(':
                        break
                    else:
                        cntalpha+=cnt.pop()
                cnt.append(a[i]) 
if len(cnt)!=0:
    for i in range(len(cnt)):
        cntalpha+=cnt.pop()
print(cntalpha)
