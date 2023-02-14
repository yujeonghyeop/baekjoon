import sys
from collections import deque
m,n,h  = map(int, sys.stdin.readline().split())
tomato = [[] for _ in range(h)]
dx = [0,-1,0,1]
dy = [-1,0,1,0]
dz = [-1,1]
dq = deque()
ans = 0
for j in range(h):
    for i in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        tomato[j].append(a)
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                dq.append([k,i,j])
while(len(dq)!=0):
    print(tomato)
    a,b,c = dq.popleft()
    for k in range(4):
        if b + dx[k] >= 0 and b + dx[k] <= n-1 and c + dy[k] >= 0 and c + dy[k] <= m-1 and tomato[a][b+dx[k]][c+dy[k]]==0:
            tomato[a][b+dx[k]][c+dy[k]] = tomato[a][b][c] +1
            dq.append([a,b+dx[k],c+dy[k]])
    for k in range(2):
        if a + dz[k] >=0 and a + dz[k] <= h-1 and tomato[a+dz[k]][b][c] == 0:
            tomato[a+dz[k]][b][c] = tomato[a][b][c] + 1
            dq.append([a+dz[k],b,c])
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 0:
                print(-1)
                quit()
        ans = max(ans, max(tomato[k][i]))
print(ans-1)