import sys 
sys.setrecursionlimit(10**7)
def dfs(road, x, y,count,cost):
    if count == 3:
        if cost[x][y] >=2:
            print(1)
            exit()
        else:
            return
    ddx = [0,-1,0,1]
    ddy = [-1,0,1,0]
    for i in range(4):
        dx = x + ddx[i]
        dy = y + ddy[i]
        if dx < 0 or dx > 4 or dy < 0 or dy > 4:
            continue
        if road[dx][dy] == -1:
            continue
        if road[dx][dy] == 1:
            cost[dx][dy] = max(cost[dx][dy], cost[x][y]+1)
        else:
            cost[dx][dy]= max(cost[dx][dy], cost[x][y])
        road[x][y] = -1
        dfs(road, dx,dy,count +1,cost)
    return True
road = []
for i in range(5):
    a = list(map(int,sys.stdin.readline().split()))
    road.append(a)
x,y = map(int, sys.stdin.readline().split())
count = 0
cost = [[0]*5 for _ in range(5)]
dfs(road,x,y,count,cost)

print(0)