import sys

N, K = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
diff = []
sum = 0
for i in range(0, N-1):
    diff.append(a[i+1] - a[i])
diff = sorted(diff)
for j in range(0,N-K):
    sum += diff[j]
print(sum)
