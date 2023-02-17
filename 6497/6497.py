import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
while True:
    m, n = map(int, sys.stdin.readline().split())
    if m==0 and n==0:
        break
    parent = [i for i in range(m)]
    houserarr = []
    cost = 0
    for i in range(n):
        a,b,c = map(int, sys.stdin.readline().split())
        houserarr.append([a,b,c])
    housearr = sorted(houserarr, key = lambda x: x[2])
    for i in housearr:
        u,v,w = i
        if find(u) != find(v):
            union(u,v)
        else:
            cost += w
    print(cost)
