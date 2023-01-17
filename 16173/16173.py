import sys

def dfs(n,room,x,y,visited):
    cnt = room[x][y]
    if cnt == -1:
        print("HaruHaru")
        exit()
    for i in range(2):
        if x+cnt<n and visited[x+cnt][y]==0:
            visited[x+cnt][y] = 1
            dfs(n,room,x+cnt,y,visited)
            visited[x+cnt][y]=0
        if y+cnt < n and visited[x][y+cnt] ==0:
            visited[x][y+cnt] = 1
            dfs(n, room,x, y+cnt,visited)
            visited[x][y+cnt] = 0

n = int(sys.stdin.readline())
room = [ ]
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    room.append(a)
visited = [[0]*n for _ in range(n)]
visited[0][0] = 1
dfs(n,room, 0,0,visited)
print("Hing")