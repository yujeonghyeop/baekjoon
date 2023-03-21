import sys
sys.setrecursionlimit(10**6)

def dfs(n,m,a):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visited[n][m] = 1
    for i in range(4):
        ddx = n + dx[i]
        ddy = m + dy[i]
        if ddx < 0 or ddx >=R or ddy < 0 or ddy >= C:
            continue
        elif field[ddx][ddy] == "#":
            continue
        elif field[ddx][ddy] == "." and visited[ddx][ddy] == 0:
            dfs(ddx,ddy,a)
        elif field[ddx][ddy] == "v" and visited[ddx][ddy] == 0:
            a.append("v")
            dfs(ddx,ddy,a)
        elif field[ddx][ddy] == "k" and visited[ddx][ddy] == 0:
            a.append("k")
            dfs(ddx,ddy,a)

R,C = map(int, sys.stdin.readline().split())
field = [[]for _ in range(R)]
visited = [[0]*C for _ in range(R)]
wolf = 0
sheep = 0
for i in range(R):
    a = list(sys.stdin.readline().split())
    for j in a[0]:
        field[i].append(j)
for i in range(R):
    for j in range(C):
        animal = []
        if field[i][j] == "v" or field[i][j] == "k":
            if visited[i][j] == 0:
                animal.append(field[i][j])
                dfs(i,j,animal)
                v = animal.count('v')
                k = animal.count('k')
                if v<k:
                    sheep += k
                else:
                    wolf += v
print(sheep,wolf)