import sys

a,b = map(int,sys.stdin.readline().split())

n = 1
m = 1
cnt = 1
for i in range(a-1):
    if i == 0 :
        continue
    elif i == 1:
        continue
    else:
        cnt = n+m
        n = m
        m = cnt
lim = b // n
for j in range(1,lim):
    moc = b - (n*j)
    if moc % cnt == 0:
        print(j)
        print(moc//cnt)
        break