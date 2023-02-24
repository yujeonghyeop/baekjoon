import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
farm = [[]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)
distance = {}
dis = 0
q = deque()
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    farm[a].append(b)
    farm[b].append(a)
q.append(farm[1])
visited[1] = 1
while(q):
    dis+=1
    cntar = []
    cnt = q.popleft()
    for i in cnt:
        visited[i] = 1
    for i in cnt:
        if dis not in distance:
            distance[dis] = [i]
        else:
            distance[dis].append(i)
        for j in farm[i]:
            if visited[j] == 0:
                cntar.append(j)
    if len(cntar) !=0:
        q.append(list(set(cntar)))
answer = sorted(distance[dis])
print(answer[0], dis, len(distance[dis]))
