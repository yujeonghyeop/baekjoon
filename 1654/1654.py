import sys
a, b = map(int, sys.stdin.readline().split())
cnt = []
ranswer = []
for i in range(a):
    cnt.append(int(sys.stdin.readline()))
start=1
end = max(cnt)
while(end>=start):
    mid = (start+end)//2
    d = 0
    for k in range(len(cnt)):
        d+= cnt[k]//mid
    if d>=b:
        start=mid+1
    else:
        end=mid-1
print(end)
