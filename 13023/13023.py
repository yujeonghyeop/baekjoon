from collections import deque
def dfs(start,depth):
    global ans
    visited[start]=True
    if depth>=4:
        ans= True
        return
    if ans:
        return
    for i in cnt[start]:
        if visited[i]==False:
            dfs(i,depth+1)
            visited[i]=False

a,b = map(int,input().split())
cnt = [[]for x in range(a)]
visited = [False]*a
depthlist=[0]
route = [[]for x in range(a)]
for i in range(b):
    c,d = map(int,input().split())
    cnt[c].append(d)
    cnt[d].append(c)
ans = False
for i in range(a):
    dfs(i,0)
    visited[i] = False
    if ans:
        break
print(1 if ans else 0)