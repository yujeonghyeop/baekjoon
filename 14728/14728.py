import sys

N,T = map(int, sys.stdin.readline().split())
times = []
scores = []
dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
for i in range(N):
    t,s = map(int,sys.stdin.readline().split())
    scores.append(s)
    times.append(t)
for i in range(1,N+1):
    for j in range(1,T+1):
        if j >=times[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-times[i-1]] + scores[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][T])