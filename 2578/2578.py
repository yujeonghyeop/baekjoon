import sys
bingo = []
ans = []
for i in range(5):
    a = list(map(int, sys.stdin.readline().split()))
    bingo.append(a)
for j in range(5):
    b = list(map(int, sys.stdin.readline().split()))
    ans+=b
for i in range(25):
    line = 0
    cnt = 0
    for j in range(5):
        for k in range(5):
            if bingo[j][k] == ans[i]:
                bingo[j][k] = 0
    for j in range(5): #가로검사
        cnt = 0
        for k in range(5):
            if bingo[j][k] == 0:
                cnt +=1
        if cnt == 5:
            line +=1
    for j in range(5): #세로검사
        cnt = 0
        for k in range(5):
            if bingo[k][j] == 0:
                cnt +=1
        if cnt == 5:
            line +=1
    cnt = 0
    for j in range(5): #00,11,22,33,44/ 04,13,22,31,40
        if bingo[j][j] == 0:
            cnt +=1
        if cnt == 5:
            line +=1
    cnt = 0
    for j in range(5):
        if bingo[j][4-j] == 0:
            cnt +=1
        if cnt == 5:
            line +=1
    if line >=3:
        print(i+1)
        break  

