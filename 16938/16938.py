import sys
from itertools import combinations
N,L,R,X = map(int,sys.stdin.readline().split())
problem = []
a = list(map(int,sys.stdin.readline().split()))
problem.append(a)
test = []
answer = 0
for i in range(2,N+1):
    for j in combinations(a,i):
        test.append(j)
for i in test:
    sumcondition = sum(i)
    levelcondition = max(i) - min(i)
    if L<=sumcondition<=R and X<=levelcondition:
        answer+=1
print(answer)
