import sys
import collections


n = int(input())
q = collections.deque()
friend = [[] for _ in range(n+1)]
route = [[0]*(n+1) for _ in range(n+1)]
cntmax = []
man = []
while(True):
    a,b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    else:
        friend[a].append(b)
        friend[b].append(a)
def bfs(i,n):
    visited[n] = True
    q.append(n)
    while q:
        x = q.popleft()
        for j in friend[x]:
            if not visited[j]:
                q.append(j)
                route[i][j] = route[i][x] + 1
                visited[j] = True

for i in range(n):
    visited = [False] * (n+1)
    bfs(i+1,i+1)
for p in range(n+1):
    for q in range (n+1):
        if route[p][q] !=0:
            if route[q][p] == 0:
                route[q][p] = route[p][q]
            else:
                route[q][p] = min(route[p][q], route[q][p])
                route[p][q] = route[q][p]
for i in range(1,n+1):
    a = max(route[i])
    cntmax.append(a)
cntmax = sorted(cntmax)
for i in range(1, n+1):
    if max(route[i]) == cntmax[0]:
        man.append(i)
man = sorted(man)
print("{} {}".format(cntmax[0],len(man)))
print(*man)
    