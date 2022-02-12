import sys

a,b = list(map(int, sys.stdin.readline().split()))
poketmon = {}
for i in range(a):
    c=input()
    poketmon[c] = i
e = list(poketmon.items())
for i in range(b):
    a = input()
    if a.isalpha() != True:
        cnt = int(a)-1
        print(e[cnt][0])
    else:
        print(poketmon[a]+1)