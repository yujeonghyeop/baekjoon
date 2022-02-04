import sys
while(True):
    a= input()
    stackb = []
    if a==".":
        break
    for i in a:
        if i==".":
            if len(stackb)==0:
                print("yes")
            else:
                print("no")
            break
        if i=="(":
            stackb.append(i)
        elif i==")":
            if len(stackb)==0:
                print("no")
                break
            elif stackb[-1]!="(":
                print("no")
                break
            else:
                stackb.pop()
        if i=="[":
            stackb.append(i)
        elif i=="]":
            if len(stackb)==0:
                print("no")
                break
            elif stackb[-1]!="[":
                print("no")
                break
            else:
                stackb.pop()