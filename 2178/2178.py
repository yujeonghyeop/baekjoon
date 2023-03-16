import sys
from collections import deque
N,M  = map(int, sys.stdin.readline().split())
miro = []
visited = [[0]*M for _ in range(N)]

def dfs(a,b):
    visited[a][b] = 1
    q = deque()
    q.append([a,b])
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while(q):
        x,y = q.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx < 0 or ddx >= N or ddy < 0 or ddy >=M:
                continue
            elif miro[ddx][ddy] == '1' and visited[ddx][ddy] == 0:
                visited[ddx][ddy] = visited[x][y] + 1
                q.append([ddx,ddy])


for i in range(N):
    cnt = []
    a = list(sys.stdin.readline().split())
    for j in range(M):
        cnt.append(a[0][j])
    miro.append(cnt)

dfs(0,0)
print(visited[N-1][M-1])