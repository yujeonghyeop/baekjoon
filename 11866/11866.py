import sys
a, b = map(int, sys.stdin.readline().split())
cnt = []
c = 0
answer = []
for i in range(1, a+1):
    cnt.append(i)
print(cnt)
for i in range(len(cnt)):
    c = (c + b - 1) % len(cnt)
    answer.append(cnt[c])
    del cnt[c]
    print(cnt)
print("<", end='')
for j in range(len(answer)):
    if j != len(answer)-1:
        print(answer[j], end='')
        print(',', end=' ')
    else:
        print(answer[j], end='')
print(">")
