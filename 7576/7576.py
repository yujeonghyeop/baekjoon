import sys
from collections import deque
m,n  = map(int, sys.stdin.readline().split())
tomato = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]
visited = [[0]*m for _ in range(n)]
dq = deque()
ans = 0
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    tomato.append(a)
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append([i,j])
while(len(dq)!=0):
    print(tomato,visited)
    a,b = dq.popleft()
    for k in range(4):
        if a + dx[k] >= 0 and a + dx[k] <= n-1 and b + dy[k] >= 0 and b + dy[k] <= m-1 and tomato[a+dx[k]][b+dy[k]]==0:
            tomato[a+dx[k]][b+dy[k]] = tomato[a][b] +1
            dq.append([a+dx[k],b+dy[k]])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            quit()
    ans = max(ans, max(tomato[i]))
print(ans-1)