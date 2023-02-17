import sys

M, N = map(int, sys.stdin.readline().split())

bee = [[1]*M for _ in range(M)]
grow = []
growarray = [0]*(2*M-1)
for i in range(N):
    a,b,c = map(int, sys.stdin.readline().split())
    for w in range(a, a+b):
        growarray[w] += 1
    for w in range(a+b, 2*M-1):
        growarray[w] += 2
print(growarray)
for j in range(M-1,-1,-1):
    bee[j][0] += growarray[(M-1)-j]
for l in range(1, M):
    bee[0][l] += growarray[l+(M-1)]
print(bee)
for x in range(1,M):
    for y in range(1,M):
        bee[x][y] += bee[0][y] - 1
for i in bee:
    print(*i)
