strlist = []
calstrlist = []
n = int(input())
alphadict = {}
for i in range(n):
    a = str(input())
    strlist.append(a)
    calstrlist.append(a)
for i in range(len(strlist)):
    callen = len(strlist[i])
    for j in range(len(strlist[i])):
        if strlist[i][j] not in alphadict:
            alphadict[strlist[i][j]] = 10**(callen-1)
        else:
            alphadict[strlist[i][j]] += 10**(callen-1)
        callen -= 1
alphadict = sorted(alphadict.items(), key = lambda x:x[1], reverse=True)
changealpha = {}
num = 10
for i in alphadict:
    num -= 1
    changealpha[i[0]] = num
calc = []
for k in calstrlist:
    for q in range(len(k)):
        if k[q] in changealpha:
            k = k.replace(k[q], str(changealpha[k[q]]))
    calc.append(int(k))
print(sum(calc))
