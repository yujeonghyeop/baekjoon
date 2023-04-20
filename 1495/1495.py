import sys

N,S,M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1
answer = -1
for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            if j + a[i] <= M:
                dp[i+1][j+a[i]] = 1
            if j - a[i] >=0:
                dp[i+1][j-a[i]] = 1
for k in range(M,-1,-1):
    if dp[N][k] == 1:
        answer = k
        break
print(answer)