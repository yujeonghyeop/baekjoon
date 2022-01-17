import sys
a, b = map(int, sys.stdin.readline().split())
cnt = [[0]*(b+1) for i in range(a+1)]
for i in range(1, len(cnt)):
    if len(cnt[0])>=2:
        cnt[i][1] = 1
for j in range(1, len(cnt[0])):
    cnt[0][j] = 1
    if len(cnt)>=2:
        cnt[1][j] = j
for i in range(2, a+1):
    for j in range(2, b+1):
        cnt[i][j] = cnt[i-1][j] + cnt[i][j-1]
print(cnt[a][b]%1000000000)
