import sys
import itertools

N,K = sys.stdin.readline().split()
health = list(map(int, sys.stdin.readline().split()))
nPr = list(itertools.permutations(health,int(N)))

count = 0
for i in range(len(nPr)):
    base = 500
    status = 0
    for j in range(int(N)):
        base -= int(K)
        base += nPr[i][j]
        if base < 500:
            break
        else:
            status +=1
    if status ==int(N):
        count +=1
print(count)
