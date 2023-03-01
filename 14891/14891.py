import sys
from collections import deque
topni =[]
for i in range(4):
    cnt = deque()
    a = sys.stdin.readline().split()
    for j in range(len(a[0])):
        cnt.append(a[0][j])
    topni.append(cnt)
n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    command = []
    cnt = a-1
    if cnt == 0:
        command.append([0,b])
        b = b*-1
        for j in range(3):
            if topni[j][2] == topni [j+1][6]:
                break
            else:
                command.append([j+1,b])
                b = b*-1
    elif cnt == 1:
        command.append([1,b])
        b = b*-1
        if topni[0][2] != topni[1][6]:
            command.append([0,b])
        if topni[1][2] != topni[2][6]:
            command.append([2,b])
            b = b*-1
            if topni[2][2] != topni[3][6]:
                command.append([3,b])
    elif cnt == 2:
        command.append([2,b])
        b = b*-1
        if topni[2][2] != topni[3][6]:
            command.append([3,b])
        if topni[2][6] != topni[1][2]:
            command.append([1,b])
            b = b*-1
            if topni[0][2] != topni[1][6]:
                command.append([0,b])
    elif cnt == 3:
        command.append([3,b])
        b = b*-1
        for j in range(3,0,-1):
            if topni[j][6] == topni[j-1][2]:
                break
            else:
                command.append([j-1,b])
                b = b*-1
    for k in command:
        c,d = k
        if d == -1:
            out = topni[c].popleft()
            topni[c].append(out)
        elif d == 1:
            out = topni[c].pop()
            topni[c].appendleft(out)
answer = 0
n = 1
for i in range(4):
    if topni[i][0] == '1':
        answer += n
    n = n*2
print(answer)