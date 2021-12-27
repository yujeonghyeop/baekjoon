import sys
import collections
a = collections.deque()
n = int(sys.stdin.readline())
for i in range(n):
    read = sys.stdin.readline().split()
    if read[0] == 'push_back':
        a.append(read[1])
    elif read[0] == 'push_front':
        a.appendleft(read[1])
    elif read[0] == 'pop_front':
        if len(a) != 0:
            print(a.popleft())
        else:
            print(-1)
    elif read[0] == 'pop_back':
        if len(a) != 0:
            print(a.pop())
        else:
            print(-1)
    elif read[0] == 'size':
        print(len(a))
    elif read[0] == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif read[0] == 'front':
        if len(a) != 0:
            print(a[0])
        else:
            print(-1)
    elif read[0] == 'back':
        if len(a) != 0:
            print(a[-1])
        else:
            print(-1)
