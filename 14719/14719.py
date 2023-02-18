import sys

m,n = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
world = [[0]*n for _ in range(m)]
status = True
answer = 0
for i in range(n):
    for j in range(m-1, m-1-a[i],-1):
        world[j][i] = 1
for i in range(m):
    cnt = 0
    status = True
    for j in range(n-1):
        if world[i][j] == 1 and world[i][j+1] == 0:
            status = False
        elif status == False and world[i][j] == 0 and world[i][j+1] == 1:
            cnt+=1
            status = True
            answer += cnt
            cnt = 0
        elif world[i][j] == 0 and status == False:
            cnt+=1
print(answer)