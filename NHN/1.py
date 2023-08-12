import sys
from collections import deque
def bfs(a,b):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    q = deque()
    q.append([a,b])
    visited[a][b] = 0
    while(len(q) != 0):
        x,y = q.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx < 0 or ddy < 0 or ddx >= len(car) or ddy >= len(car[0]):
                continue
            elif car[ddx][ddy] == 3:
                continue
            elif car[ddx][ddy] == 4:
                if visited[ddx][ddy] == 999:
                    visited[ddx][ddy] = visited[x][y]
                else:
                    visited[ddx][ddy] = min(visited[ddx][ddy], visited[x][y])
                break
            elif car[ddx][ddy] == 0:
                if visited[ddx][ddy] == 999:
                    visited[ddx][ddy] = visited[x][y]
                    q.append([ddx,ddy])
                else:
                    if visited[ddx][ddy] > visited[x][y]:
                        visited[ddx][ddy] = visited[x][y]
                        q.append([ddx,ddy])
            elif car[ddx][ddy] == 2:
                if visited[ddx][ddy] == 999:
                    visited[ddx][ddy] = visited[x][y] + 1
                    q.append([ddx,ddy])
                else:
                    if visited[ddx][ddy] > visited[x][y]+1:
                        visited[ddx][ddy] = visited[x][y]+1
                        q.append([ddx,ddy])

# car =[
#     [0,0,3,0,0,0,0], 
#     [1,0,3,0,0,0,0],
#     [0,0,3,0,0,0,0],
#     [0,0,2,0,0,3,3],
#     [2,2,2,0,2,0,0],
#     [3,3,2,0,2,0,3],
#     [3,3,2,0,2,0,4]]
car = [[0,2,0,0,0],[0,4,2,0,0],[0,2,0,0,0],[0,0,0,2,1],[0,0,0,2,0]]
# car = [[0,0,0,0,0],[3,0,0,0,0],[4,3,0,0,0],[0,0,3,0,0],[0,0,0,3,1]]

visited = [[999]* len(car[0]) for _ in range(len(car))]
start = []
end = []
for i in range(len(car)):
    for j in range(len(car[0])):
        if car[i][j] == 1:
            start.append([i,j])
        elif car[i][j] == 4:
            end.append([i,j])
bfs(start[0][0], start[0][1])
print(visited)
if visited[end[0][0]][end[0][1]] == 999:
    print(-1)
else:
    print(visited[end[0][0]][end[0][1]])