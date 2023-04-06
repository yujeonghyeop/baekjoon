#8
# 1 6 2 5 7 3 5 6

import sys

N = int(input())
a = list(map(int, sys.stdin.readline().split()))
dp = [1] * N
dp[0] = 1
for i in range(1,len(a)):
    cnt = []
    for j in range(i):
        if a[i] > a[j]:
            cnt.append(dp[j] +1)
    if len(cnt) != 0:
        dp[i] = max(cnt)
    print(i,a[i], dp)

print(max(dp))