import sys
import heapq
INF = int(1e9)
def dij(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0,start))
    while queue:
        currentdis, currentdest = heapq.heappop(queue)
        if distance[currentdest] < currentdis:
            continue
        for i in room[currentdest]:
            cost = currentdis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))

n = int(input())
for i in range(n):
    N,M = map(int,sys.stdin.readline().split())
    room = [[] for _ in range(N+1)]
    total = [0] * (N+1)
    for j in range(M):
        a,b,c = map(int,sys.stdin.readline().split())
        room[a].append([b,c])
        room[b].append([a,c])
    K = int(input())
    friend = list(map(int,sys.stdin.readline().split()))
    for i in friend:
        distance = [INF] * (N+1)
        dij(i)
        for j in range(1, N+1):
            total[j] += distance[j]
    cnt = INF
    minindex = 0
    for i in range(1,len(total)):
        if total[i] < cnt:
            cnt = total[i]
            minindex = i
    print(minindex)
