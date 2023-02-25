import sys

a,b = map(int, sys.stdin.readline().split())
maps = []
dp = [[0]*b for _ in range(a)]
print(dp)
for i in range(a):
    c = list(map(int, sys.stdin.readline().split()))
    maps.append(c)
dp[0][0] = maps[0][0]
if a==1:
    print(sum(maps[0]))
else:
    for i in range(a-1):
        for j in range(b-1):
            dp[i][j+1] = max(dp[i][j+1],dp[i][j] + maps[i][j+1])
            dp[i+1][j] = max(dp[i+1][j],dp[i][j] + maps[i+1][j])
            dp[i+1][j+1] = max(dp[i][j+1] + maps[i+1][j+1], dp[i+1][j] + maps[i+1][j+1])
            print(dp)
    print(dp[a-1][b-1])
