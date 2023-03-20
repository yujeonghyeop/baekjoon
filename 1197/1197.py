import sys
def parent(x):
    if graph[x] == x:
        return x
    graph[x] = parent(graph[x])
    return graph[x]
def union(a,b):
    a = parent(a)
    b = parent(b)
    if a<b:
        graph[b] = a
    else:
        graph[a] = b
n, m = map(int,sys.stdin.readline().split())
graph = [0]*(n+1)
arr = []
answer = 0
for i in range(n+1):
    graph[i] = i
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    arr.append([a,b,c])
arr = sorted(arr, key = lambda x:x[2])
for i in arr:
    a,b,c = i
    if parent(a) != parent(b):
        union(a,b)
        answer+=c
print(answer)
