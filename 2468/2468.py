import sys
from collections import deque

def bfs(arr,x,y,c):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q=deque()
    q.append([x,y])
    visited[x][y] = c
    while(q):
        a,b = q.popleft()
        for i in range(4):
            ddx = a + dx[i]
            ddy = b + dy[i]
            if ddx < 0 or ddx >= N or ddy < 0 or ddy >= N:
                continue
            else:
                if arr[ddx][ddy] !=0 and visited[ddx][ddy] == -1:
                    visited[ddx][ddy] = c
                    q.append([ddx,ddy])

N = int(input())
town = []
maxnumber = -1
answer = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    if max(a) > maxnumber:
        maxnumber = max(a)
    town.append(a)

for i in range(1,maxnumber):
    cnt = []
    visited = [[-1]*N for _ in range(N)]
    count = 1
    tocal = []
    for j in range(N):
        ccnt = []
        for k in range(N):
            if town[j][k] > i:
                ccnt.append(town[j][k])
            else:
                ccnt.append(0)
        cnt.append(ccnt)
    for p in range(N):
        for q in range(N):
            if cnt[p][q] != 0 and visited[p][q] == -1:
                bfs(cnt,p,q,count)
                count+=1
    for s in range(N):
        for l in range(N):
            if visited[s][l] not in tocal and visited[s][l] != -1:
                tocal.append(visited[s][l])

    answer.append(len(tocal))
if len(answer) !=0:
    print(max(answer))
else:
    print(1)
