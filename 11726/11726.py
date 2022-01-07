import sys

a = int(sys.stdin.readline())
d = [0] * (a+2)
d[1] = 1
d[2] = 2
for i in range(3, a+1):
    d[i] = d[i-1] + d[i-2]
print(d[a]%10007)