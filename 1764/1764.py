import sys
a, b = list(map(int, sys.stdin.readline().split()))
cnt = {}
ranswer = []
for i in range(a):
    cnt[input()] = 1
for j in range(b):
    e = input()
    if e in cnt:
        cnt[e] += 1
    else:
        cnt[e] = 1
answer = list(cnt.items())
print(answer)
for i in range(len(answer)):
    if answer[i][1] == 2:
        ranswer.append(answer[i][0])
print(len(ranswer))
ranswer.sort()
for i in range(len(ranswer)):
    print(ranswer[i])
