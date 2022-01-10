import sys
n = int(sys.stdin.readline())
array = []
for i in range(n):
    a = int(sys.stdin.readline())
    array.append(a)
cnt = max(array)
dp = [[0]*3 for i in range(100000)]
dp[0] = [0, 0, 0]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
for j in range(4, cnt+1):
    dp[j][0] = dp[j-1][1] % 1000000009 + dp[j-1][2] % 1000000009
    dp[j][1] = dp[j-2][0] % 1000000009 + dp[j-2][2] % 1000000009
    dp[j][2] = dp[j-3][0] % 1000000009 + dp[j-3][1] % 1000000009
for k in range(len(array)):
    print(sum(dp[array[k]]) % 1000000009)
