import sys
n = int(sys.stdin.readline())
read = sys.stdin.readline().split()
d = {}
for i in range(n):
    if int(read[i]) in d:
        d[int(read[i])] += 1
    else:
        d[int(read[i])] = 1
m = int(sys.stdin.readline())
cnt = sys.stdin.readline().split()
for i in range(m):
    if int(cnt[i]) in d:
        print(d[int(cnt[i])], end=' ')
    else:
        print(0, end=' ')
