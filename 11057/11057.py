import sys
dp = [[1,1,1,1,1,1,1,1,1,1]for x in range(1002)]
n = int(sys.stdin.readline())
for i in range(2,n+1):
    for j in range(1,10):
        dp[i][j] =  dp[i][j-1] + dp[i-1][j]
print(sum(dp[n])%10007)
