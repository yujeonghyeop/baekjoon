import sys
n = int(sys.stdin.readline())
for i in range(n):
    read = sys.stdin.readline().split()
    for j in range(len(read)):
        a = read[j]
        print(a[::-1], end=' ')
