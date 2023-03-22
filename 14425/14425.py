import sys

N,M = map(int,sys.stdin.readline().split())
check = []
arr = []
answer = 0
for i in range(N):
    a = sys.stdin.readline().split()
    check.append(a)
for j in range(M):
    b = sys.stdin.readline().split()
    arr.append(b)
for k in arr:
    if k in check:
        answer+=1
print(answer)