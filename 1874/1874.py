import sys
n = int(sys.stdin.readline())
cnt = []
answer = []
realanswer = []
check = True
k = 0
for i in range(n):
    a = int(sys.stdin.readline())
    if a > k:
        for j in range(k+1, a+1):
            answer.append(j)
            realanswer.append('+')
        answer.pop()
        realanswer.append('-')
        k = a
    else:
        if len(answer) == 0:
            check = False
        for p in range(len(answer)):
            if answer[-1] == a:
                answer.pop()
                realanswer.append('-')
                break
            else:
                answer.pop()
                realanswer.append('-')
if check == True:
    for i in range(len(realanswer)):
        print(realanswer[i])
else:
    print('NO')
