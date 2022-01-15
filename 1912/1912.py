import sys
n = int(sys.stdin.readline())
read = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n)
dp[0] = read[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+read[i], read[i])
print(max(dp))
