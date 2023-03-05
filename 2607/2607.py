n = int(input())
compare = input()
answer = 0
for i in range(n-1):
    b = input()
    tempcompare = compare
    if abs(len(compare) - len(b)) > 1:
        continue
    elif len(compare) > len(b):
        b += '0'
    elif len(compare) < len(b):
        tempcompare += '0'
    comparearr = sorted(list(tempcompare))
    barr = sorted(list(b))
    for j in comparearr:
        if j in barr:
            barr.remove(j)
    if len(barr) == 0 or len(barr) == 1:
        answer+=1
print(answer)