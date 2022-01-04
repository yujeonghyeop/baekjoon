import sys
import math
min = 1000000000
a, b = map(int, sys.stdin.readline().split())
count = 1
read = list(map(int, sys.stdin.readline().split()))
for j in range(len(read)):
    if abs(b-read[j]) < min:
        min = abs(b-read[j])
        minindex = j
min = 1000000000
cnt = abs(b - read[minindex])
cnt1 = read[minindex]
del read[minindex]
if a == 1:
    print(cnt)
else:
    while(len(read) != 0):
        for k in range(len(read)):
            if abs(cnt1 - read[k]) < min:
                min = abs(cnt1 - read[k])
                minindex = k
        cnt2 = abs(cnt1 - read[minindex])
        cnt1 = read[minindex]
        del read[minindex]
        if count == 1:
            gcd = math.gcd(cnt, cnt2)
            count+=1
        else:
            gcd = math.gcd(gcd,cnt2)
    print(gcd)
