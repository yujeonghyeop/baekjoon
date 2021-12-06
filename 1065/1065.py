def hansu(a):
    a = str(a)
    if len(a) <= 2:
        return a
    else:
        cnt = int(a[1])-int(a[0])
        check = True
        for i in range(len(a)-1):
            if int(a[i+1])-int(a[i]) != cnt:
                check = False
        if check:
            return int(a)


num = int(input())
answer = []
for i in range(1, num+1):
    if hansu(i):
        answer.append(hansu(i))
print(len(answer))
