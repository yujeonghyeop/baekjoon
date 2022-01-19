import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))
b = max(a)
cnt = [0]*(b+1)
cnt[1] = 1
cnt[2] = 2
cnt[3] = 4
for j in range(4, b+1):
    cnt[j] = cnt[j-1] % 1000000009 + cnt[j-2] % 1000000009 + cnt[j-3] % 1000000009
for i in range(len(a)):
    print((cnt[a[i]]) % 1000000009)
