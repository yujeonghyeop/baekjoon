import sys
read = sys.stdin.readline().split()
answer = []
cnt = []
a = -1
for i in range(1, int(read[0])+1):
    answer.append(i)
for j in range(len(answer)):
    a += int(read[1])
    a = a % len(answer)
    cnt.append(answer[a])
    del answer[a]
    a -= 1
print('<', end='')
for k in range(len(cnt)):
    if k != len(cnt)-1:
        print(cnt[k], end=', ')
    else:
        print(cnt[k], end='>')
