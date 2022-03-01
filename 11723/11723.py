import sys
n = int(sys.stdin.readline())
s = [0]*21
for i in range(n):
    read = sys.stdin.readline().split()
    if len(read) >= 2:
        read[1] = int(read[1])
    if read[0] == 'add':
        if s[read[1]] == 0:
            s[read[1]] = 1
    elif read[0] == 'remove':
        if s[read[1]] == 1:
            s[read[1]] = 0
    elif read[0] == 'check':
        if s[read[1]] == 1:
            print(1)
        else:
            print(0)
    elif read[0] == 'toggle':
        if s[read[1]] == 1:
            s[read[1]] = 0
        else:
            s[read[1]] = 1
    elif read[0] == 'all':
        for i in range(len(s)):
            s = [1]*21
    elif read[0] == 'empty':
        for i in range(len(s)):
            s = [0]*0
