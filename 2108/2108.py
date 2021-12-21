from collections import Counter
n = int(input())
a = []
cnt = []
for i in range(n):
    a.append(int(input()))
a = sorted(a)
print(int(round(sum(a)/n, 0)))
b = Counter(a).most_common()
print(a[n//2])
print(b)
print(max(a)-min(a))
