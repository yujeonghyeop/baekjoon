import sys
from collections import deque
sys.setrecursionlimit(10 ** 4)
def earthSick():
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for j in range(N):
        for k in range(M):
            count = 0
            if board[j][k] != 0:
                for i in range(4):
                    nx = j + dx[i]
                    ny = k + dy[i]
                    if nx < 0 or ny < 0 or nx >= N or ny >= M:
                        continue
                    elif board[nx][ny] == 0:
                        count += 1 
                board[j][k] -= count
                if board[j][k] == 0:
                    board[j][k] = -1
    for i in range(N):
        for j in range(M):
            if board[i][j] < 0:
                board[i][j] = 0

def checkTwo(x,y,visited):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q= deque()
    q.append([x,y])
    visited[x][y] = 1
    while(len(q) != 0):
        nx,ny = q.popleft()
        for i in range(4):
            ddx = nx + dx[i]
            ddy = ny + dy[i]
            if ddx < 0 or ddy < 0 or ddx >= N or ddy >= M:
                continue
            elif board[ddx][ddy] != 0 and visited[ddx][ddy] == 0:
                q.append([ddx,ddy])
                visited[ddx][ddy] = 1 


N, M = map(int, sys.stdin.readline().split())
board = []
answer = 1
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    board.append(a)

while(True):
    earthSick()
    cnt = 0
    glacier = 0
    Checkvisited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            glacier += board[i][j]
            if board[i][j] != 0 and Checkvisited[i][j] == 0:
                checkTwo(i,j,Checkvisited)
                cnt += 1
    if cnt >= 2:
        break
    if glacier == 0:
        answer = 0
        break
    answer +=1
print(answer)