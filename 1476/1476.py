import sys
a, b, c = sys.stdin.readline().split()
string = a+b+c
year = 0
e = 0
s = 0
m = 0
i = 0
while(True):
    e += 1
    s += 1
    m += 1
    i += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    if str(e) + str(s) + str(m) == string:
        print(i)
        print(str(e)+str(s)+str(m), string)
        break
