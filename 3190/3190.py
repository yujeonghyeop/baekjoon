import sys
from collections import deque
N = int(input())
K = int(input())
apple = []
for i in range(K):
    a = list(map(int, sys.stdin.readline().split()))
    a[0] -= 1
    a[1] -= 1 
    apple.append(a)
L = int(input())
snake = deque()
for i in range(L):
    b = list(sys.stdin.readline().split())
    snake.append(b)
visited = [[0 for _ in range(N)] for _ in range(N)]
board = [[0 for _ in range(N)] for _ in range(N)]
for i in range(len(apple)):
    board[apple[i][0]][apple[i][1]] = 1
dx = [-1,0,1,0]
dy = [0,-1,0,1]
dir = 3
time = 0
visited[0][0] = 1
snakelength = deque()
snakelength.append([0,0])
q= deque()
q.append([0,0])
while(True):
    time+=1
    x,y = q.popleft()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        break
    elif visited[nx][ny] == 1:
        break
    elif board[nx][ny] == 1:
        board[nx][ny] = 0
        visited[nx][ny] = 1
        snakelength.append([nx,ny])
        q.append([nx,ny])
    elif board[nx][ny] == 0:
        visited[nx][ny] = 1
        px,py = snakelength.popleft()
        visited[px][py] = 0
        snakelength.append([nx,ny])
        q.append([nx,ny])
    if len(snake) != 0:
        if int(snake[0][0]) == time:
            if snake[0][1] == 'L':
                dir = (dir + 1) % 4
            elif snake[0][1] == 'D':
                dir = (dir + 3) % 4 
            snake.popleft()
print(time)
