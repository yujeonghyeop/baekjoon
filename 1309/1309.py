import sys
n = int(sys.stdin.readline())
dp = [0]*(n+1)
dp[1] = 3
dp[2] = 7
for i in range(3, n+1):
    dp[i] = dp[i-1]*2 + dp[i-2]
print(dp[n] % 9901)
