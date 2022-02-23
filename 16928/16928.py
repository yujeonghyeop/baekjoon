import re
import sys
a,b = list(map(int, sys.stdin.readline().split()))
good = []
bad = []
for i in range(a):
    n,m = list(map(int, sys.stdin.readline().split()))
    good.append([n,m])
for i in range(b):
    u,v= list(map(int, sys.stdin.readline().split()))
    bad.append([u,v])
good = sorted(good, key= lambda x:x[1],reverse=True)
print(good)