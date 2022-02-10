import sys
sys.setrecursionlimit(10**5)
def dfs(p,q,c):
    if p<0 or p>=n or q<0 or q>=m:
        return False
    if array[p][q] ==1 and visited[p][q] ==0:
        visited[p][q] = 1
        array[p][q] = c
        dfs(p+1,q,c)
        dfs(p-1,q,c)
        dfs(p,q+1,c)
        dfs(p,q-1,c)

t = int(input())
for i in range(t):
    n,m,a= list(map(int,sys.stdin.readline().split()))
    cnt=1
    array = [[0 for i in range(m)]for i in range(n)]
    visited = [[0 for i in range(m)]for i in range(n)]
    answer = []
    for i in range(a):
        x,y = list(map(int, sys.stdin.readline().split()))
        array[x][y] = 1
    for i in range(n):
        for j in range(m):
            dfs(i,j,cnt)
            cnt+=1
    for i in range(n):
        for j in range(m):
            if array[i][j] != 0 and array[i][j] not in answer:
                answer.append(array[i][j])
    print(len(answer))


    
    