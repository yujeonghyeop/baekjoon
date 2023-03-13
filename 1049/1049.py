import sys

N,M = map(int, sys.stdin.readline().split())
all = []
one = []
money = 0
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    all.append(a)
    one.append(b)
all = sorted(all)
one = sorted(one)

while(N!=0):
    if N <=6:
        if all[0] < one[0] * N:
            money+=all[0]
        else:
            money += one[0] * N
        N = 0
    else:
        if all[0] < one[0] * 6:
            money += all[0]
        else:
            money += one[0] * 6
        N -= 6

print(money)