import sys
from collections import deque
def dfs(v,r):
    visiteddfs[v] = 1
    r.append(v+1)
    for i in arr[v]:
        if visiteddfs[i] == 0:
            dfs(i,r)
def bfs(v,r):
    visitedbfs[v] = 1
    r.append(v+1)
    q = deque()
    for i in arr[v]:
        q.append(i)
    while(q):
        cnt = q.popleft()
        if visitedbfs[cnt] == 0:
            r.append(cnt+1)
            visitedbfs[cnt] = 1
            for i in arr[cnt]:
                q.append(i)

N,M,V = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
for j in range(N):
    arr[j] = sorted(arr[j])
visiteddfs = [0] * N
rootdfs = []
visitedbfs = [0] * N
rootbfs = []
dfs(V-1,rootdfs)
bfs(V-1,rootbfs)
print(*rootdfs)
print(*rootbfs)
