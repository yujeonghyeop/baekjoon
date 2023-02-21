import sys
sys.setrecursionlimit(10**6)

N, M, k = map(int, sys.stdin.readline().split())
money = list(map(int, sys.stdin.readline().split()))
friend = []
parent = [i for i in range(N)]
cost = []
answer = 0
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    friend.append([a-1,b-1])
friend = sorted(friend)

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if money[a] < money[b]:
        parent[b] = a
    else:
        parent[a] = b
for i in friend:
    u,v = i
    if find(u) !=find(v):
        union(u,v)
for i in range(N):
    if find(i) != parent[i]:
        parent[i] = find(i)
for i in parent:
    if i not in cost:
        cost.append(i)
for j in cost:
    answer += money[j]
if answer > k:
    print("Oh no")
else:
    print(answer)