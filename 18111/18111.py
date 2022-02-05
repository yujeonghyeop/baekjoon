# 제거 2초, 쌓기 1초
import sys
n, m, b = list(map(int, input().split()))
mine = []
diction = {}
answer =[]
ranswer = []
for i in range(n):
    mine.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(m):
        if mine[i][j] in diction:
            diction[mine[i][j]] += 1
        else:
            diction[mine[i][j]] = 1
diction = sorted(diction.items(), key = lambda x:x[0],reverse = True)
maxim = diction[0][0]
for i in range(maxim+1):
    cnt = b
    time = 0
    for j in range(len(diction)):
        if i > diction[j][0]:
            diff = i - diction[j][0]
            cnt -= diff*diction[j][1]
            time += (diff * diction[j][1])
        elif i < diction[j][0]:
            diff = diction[j][0] -i
            cnt += diff*diction[j][1]
            time += (diff*diction[j][1]*2)
        else:
            continue
    if cnt < 0:
        break
    else:
        answer.append((time,i))
answer = sorted(answer,key = lambda x:x[0])
if answer[0][0] == answer[1][0]:
    a = answer[0][0]
    for i in range(len(answer)):
        if answer[i][0] == a:
            ranswer.append(answer[i])
    ranswer = sorted(ranswer, key = lambda x:x[1], reverse=True)
    print(ranswer[0][0],ranswer[0][1])
else:
    print(answer[0][0], answer[0][1])