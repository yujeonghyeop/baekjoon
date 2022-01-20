import sys
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    cnt =[]
    for j in range(2):
        read = list(map(int,sys.stdin.readline().split()))
        cnt.append(read)
    maxu = cnt[0][0]
    maxd = cnt[1][0]
    for k in range(1,a):
        cnt[0][k] = max(cnt[0][k]+cnt[1][k-1],maxd + cnt[0][k])
        cnt[1][k] = max(cnt[1][k]+cnt[0][k-1],maxu + cnt[1][k])
        if cnt[0][k]>maxu:
            maxu = cnt[0][k]
        if cnt[1][k]>maxd:
            maxd = cnt[1][k]
    print(max(cnt[0][a-1],cnt[1][a-1]))