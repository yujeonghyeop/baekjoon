import sys
from collections import deque
n = int(sys.stdin.readline())
a = deque()
for i in range(n):
    read = sys.stdin.readline().split()
    if read[0] == 'push':
        a.append(read[1])
    elif read[0] == 'pop':
        if len(a) == 0:
            print(-1)
        else:
            print(a[len(a)-1])
            a.pop()
    elif read[0] == 'size':
        print(len(a))
    elif read[0] == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif read[0] == 'top':
        if len(a) == 0:
            print(-1)
        else:
            print(a[len(a)-1])
