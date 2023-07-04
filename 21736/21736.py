import sys

def bfs(a,b):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    for i in range(4):
        ddx = a + dx[i]
        ddy = b + dy[i]
        if ddx <0 or ddy < 0 or ddx >= n or ddy >= m:
            continue
        elif school[ddx][ddy] == "X":
            continue
        elif school[ddx][ddy] == "P" and visited[ddx][ddy] == 0:
            visited[ddx][ddy] = 2
            bfs(ddx,ddy)
        elif school[ddx][ddy] == "O" and visited[ddx][ddy] == 0:
            visited[ddx][ddy] = 1
            bfs(ddx,ddy)
            

n,m = map(int, sys.stdin.readline().split())
school = []
friend = 0
for i in range(n):
    a = sys.stdin.readline().split()
    cnt = []
    for j in a[0]:
        cnt.append(j)
    school.append(cnt)
visited = [[0 for _ in range(m)] for _ in range(n)]
for j in range(n):
    for k in range(m):
        if school[j][k] == "I":
            visited[j][k] = 1
            bfs(j,k)
for i in range(n):
    for j in range(m):
        if visited[i][j] == 2:
            friend +=1
if friend == 0:
    print("TT")
else:
    print(friend)