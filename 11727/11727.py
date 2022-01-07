import sys

a = int(sys.stdin.readline())
d = [0]*1000
d[1] = 1
cnt = 1
for i in range(2, a+1):
    d[i] = d[i-1]*2+cnt
    cnt = cnt*-1
print(d[a] & 10007)
