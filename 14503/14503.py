import sys
from collections import deque
#0 - 북쪽, 1 - 동쪽, 2 - 남쪽, 3 - 서쪽
N,M =  map(int, sys.stdin.readline().split())
r,c,d =  map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    a = list(map(int,sys.stdin.readline().split()))
    board.append(a)
visited = [[0 for _ in range(M)] for _ in range(N)]
count = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque()
q.append([r,c])
while(True):
    x,y = q.popleft()
    visited[x][y] = 1
    status = False
    if board[x][y] == 0:
        count +=1
        board[x][y] = 2
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        if ddx < 0 or ddy < 0 or ddx >= N or ddy >= M:
            continue
        elif board[ddx][ddy] == 0 and visited[ddx][ddy] == 0:
            status = True
            break
    if status == True:
        if d == 0:
            d = 3
        else:
            d = d-1
        for i in range(4):
            px = x + dx[d]
            py = y + dy[d]
            if px < 0 or py < 0 or px >= N or py >= M or board[px][py] == 1 or board[px][py] == 2:
                if d == 0:
                    d = 3
                else:
                    d = d-1
            elif board[px][py] == 0 :
                q.append([px,py])
                break
    else:
        px = x - dx[d]
        py = y - dy[d]
        if px < 0 or py < 0 or px >= N or py >= M or board[px][py] == 1:
            break
        else:
            q.append([px,py])
print(count)