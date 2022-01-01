import sys
a = {}
n = int(sys.stdin.readline())
read = sys.stdin.readline().split()
for i in range(len(read)):
    a[int(read[i])] = 1
m = int(sys.stdin.readline())
cnt = sys.stdin.readline().split()
for j in range(m):
    if a.get(int(cnt[j])) == 1:
        print(1)
    else:
        print(0)
