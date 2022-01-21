import sys
n = int(sys.stdin.readline())
cnt = []
for i in range(n):
    cnt.append(int(sys.stdin.readline()))
if n == 1 or n == 2:
    print(max(cnt))
else:
    dp = [0] * 10000
    dp[0] = cnt[0]
    dp[1] = cnt[0] + cnt[1]
    dp[2] = max(cnt[1] + cnt[2], cnt[0] + cnt[2], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-3]+cnt[i-1]+cnt[i], dp[i-2] + cnt[i])
    print(max(dp))
