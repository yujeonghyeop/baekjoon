import sys
N = int(input())

for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    down = 1
    up = 1
    for j in range(a):
        down = down * (a-j)
        up = up * (b-j)
    print(up//down) 