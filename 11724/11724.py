import sys
sys.setrecursionlimit(5000)
def dfs(arrlist,i,visited,count,cntanswer):
    for node in arrlist[i]:
        if visited[i][node] ==0:
            visited[i][node] = 1
            cntanswer.append(count)
            dfs(arrlist, node, visited, count,cntanswer)
a,b = map(int, sys.stdin.readline().split())
arrlist = [[] for _ in range(a+1)]
for i in range(b):
    c, d = map(int,sys.stdin.readline().split())
    arrlist[c].append(d)
visited = [[0]*(a+1) for _ in range(a+1)]
cntanswer= []
for i in range(len(arrlist)):
    count = i
    if len(arrlist[i]) == 0:
        continue
    else:
        dfs(arrlist,i,visited,count,cntanswer)
print(len(list(set(cntanswer))))