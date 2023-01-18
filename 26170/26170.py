import sys

def dfs(road, x, y,count,apple,answer):
    if apple == 3:
        answer.append(count)
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        if ddx < 0 or ddx > 4 or ddy < 0 or ddy > 4:
            continue
        if road[ddx][ddy] == -1:
            continue
        if road[ddx][ddy] == 1:
            status = True
            apple+=1
        else:
            status = False
        cnt = road[x][y]
        road[x][y] = -1
        dfs(road, ddx,ddy,count+1, apple,answer)
        road[x][y] = cnt
        if status == True:
            apple -=1
    return answer
road = []
for i in range(5):
    a = list(map(int, sys.stdin.readline().split()))
    road.append(a)
x,y = map(int, sys.stdin.readline().split())
apple = 0
answer = []
if road[x][y] == 1:
    apple +=1
answer = dfs(road,x,y,0,apple, answer)
if len(answer) == 0:
    print(-1)
else:
    print(min(answer))