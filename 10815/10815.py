import sys

N = int(input())
sang = list(map(int,sys.stdin.readline().split()))
M = int(input())
su = list(map(int,sys.stdin.readline().split()))
sangdict = {}
for i in sang:
    sangdict[i] = 1
answer = []
for i in su:
    if i not in sangdict:
        answer.append(0)
    else:
        answer.append(1)
print(*answer)