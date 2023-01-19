import sys

def dfs(i,depth):
    depth +=1
    visit[i] = True
    if i == b:
        answer.append(depth)
    for node in chon[i]:
        if visit[node] != True:
            dfs(node,depth)

n = int(input())
a,b = map(int,sys.stdin.readline().split())
chon = [[] for _ in range(n+1)]
visit = [False] * (n+1)
answer = []
cnt = int(input())
for i in range(cnt):
    c,d = map(int,sys.stdin.readline().split())
    chon[c].append(d)
    chon[d].append(c)
dfs(a,0)
if len(answer)==0:
    print(-1)
else:
    print(answer[0]-1)