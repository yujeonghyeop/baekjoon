import sys

def dfs(j):
    visited[j] = True
    dx = [1,-1]
    for i in range(2):
        if j+ a[j]*dx[i] < 0  or j+ a[j]*dx[i] > n-1:
            continue
        else:
            cnt = j
            j = j+ a[j]*dx[i]
            dfs(j)
            j = cnt

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
start  = int(input())
start = start -1
visited = [False] * n
dfs(start)
answer  = 0
for i in visited:
    if i == True:
        answer +=1
print(answer)
