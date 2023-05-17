import sys

N = int(input())
M = int(input())
vip = []
for i in range(M):
    a = int(sys.stdin.readline())
    vip.append(a)
cntarr = []


dp = [1,2,3]
index = 0
cnt = 0
answer = 1
for i in range(1,N+1):
    cnt+=1
    if index < len(vip):
        if(vip[index]==i):
            cnt -= 1
            if(cnt != 0):
                cntarr.append(cnt)
            index +=1
            cnt = 0
if cnt!=0:
    cntarr.append(cnt)
if len(cntarr) == 0:
    print(1)
else:
    maxplace = max(cntarr)
    for i in range(3,maxplace+1):
        dp.append(dp[i-1] + dp[i-2])
    for i in cntarr:
        if i<=3:
            answer *= i
        else:
            answer *= dp[i-1]
    print(answer)