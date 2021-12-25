import sys
import collections
n = int(sys.stdin.readline())
answer = collections.deque()
for i in range(n):
    read = sys.stdin.readline().split()
    if read[0] == 'push':
        answer.append(int(read[1]))
    elif read[0] == 'pop':
        if len(answer) != 0:
            print(answer.popleft())

        else:
            print(-1)
    elif read[0] == 'size':
        print(len(answer))
    elif read[0] == 'empty':
        if len(answer) == 0:
            print(1)
        else:
            print(0)
    elif read[0] == 'front':
        if len(answer) == 0:
            print(-1)
        else:
            print(answer[0])
    elif read[0] == 'back':
        if len(answer) == 0:
            print(-1)
        else:
            print(answer[-1])
