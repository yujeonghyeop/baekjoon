import sys
n = int(input())
dp = [0] * (n+1)
for i in range(1,n+1):
    work = list(map(int, sys.stdin.readline().split()))
    for j in work[1:]:
        dp[i] = max(dp[i], dp[j] + work[0])
print(max(dp))

#     time.append(work[0])
#     for j in range(len(pre)):
#         prework[pre[j]-1].append(i)
#     indegree[i] += work[1]
# print(indegree)
# def topology_sort():
#     global answer
#     result = []
#     q = deque()
#     worktime = deque()
#     for i in range(n):
#         if indegree[i] == 0:
#             q.append(i)
#             worktime.append(answer + time[i])
#     while q:
#         print(q,worktime, answer)
#         node = q.popleft()
#         cnt = worktime.popleft()
#         if answer < cnt:
#             answer = cnt
#         result.append(node)
#         for next in prework[node]:
#             indegree[next] -= 1
#             if indegree[next] == 0:
#                 q.append(next)
#                 worktime.append(answer + time[next])
#     print(answer)
# topology_sort()    
