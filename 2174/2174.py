import sys

a, b = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())
robot = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]
visited = [[0]*a for _ in range(b)]
robotnum = 0
errorstr = []
#     W N E S
for i in range(n):
    robotnum += 1
    x, y, f = sys.stdin.readline().split()
    location = 0
    if f == "E":
        location = 2
    elif f == "N":
        location = 1
    elif f == "W":
        location = 0
    elif f == "S":
        location = 3
    x, y = int(x), int(y)
    visited[b-y][x-1] = robotnum
    robot.append([b-y, x-1, location])
for i in range(m):
    r, command, count = sys.stdin.readline().split()
    r,count = int(r), int(count)
    for j in range(count):
        if command == "L":
            robot[r-1][2] -= 1
            if robot[r-1][2] == -1:
                robot[r-1][2] = 3
        elif command == "R":
            robot[r-1][2] += 1
            if robot[r-1][2] == 4:
                robot[r-1][2] = 0
        elif command == "F":
            ddx = robot[r-1][0] + dx[robot[r-1][2]]
            ddy = robot[r-1][1] + dy[robot[r-1][2]]
            if ddx < 0  or ddx > b-1 or ddy < 0 or ddy > a-1:
                errorstr.append("Robot {} crashes into the wall".format(r))
            elif visited[ddx][ddy] != 0:
                errorstr.append("Robot {} crashes into robot {}".format(r, visited[ddx][ddy]))
            else:
                visited[robot[r-1][0]][robot[r-1][1]] = 0
                visited[ddx][ddy] = r
                robot[r-1][0] = ddx
                robot[r-1][1] = ddy
if len(errorstr) == 0:
    print("OK")
else:
    print(errorstr[0])

