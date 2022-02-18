import sys
n = int(sys.stdin.readline())
day = []
money = []
answer = []
for i in range(n):
    read = list(map(int, sys.stdin.readline().split()))
    day.append(read[0])
    money.append(read[1])
cnt =[0] * n
if day[0]-1 <n:
    cnt[day[0]-1] = money[0]
for i in range(1,n):
    if i + day[i]-1 <n:
        cnt[day[i] + i -1] = max(cnt[i-1] + money[i], cnt[day[i] + i -1])
    cnt[i] = max(cnt[i],cnt[i-1])
print(max(cnt))