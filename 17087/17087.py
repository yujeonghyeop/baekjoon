import sys
import math

a, b = map(int, sys.stdin.readline().split())
read = list(map(int, sys.stdin.readline().split()))
cnt = []
for i in read:
    cnt.append(abs(b-i))
gcd = cnt[0]
for j in range(1, len(cnt)):
    gcd = math.gcd(gcd, cnt[j])
print(gcd)
