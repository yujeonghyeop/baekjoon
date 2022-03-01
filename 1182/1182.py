import sys
import copy
a,b = list(map(int, sys.stdin.readline().split()))
read = list(map(int, sys.stdin.readline().split()))
s = []
cnt = 0
for i in range(1<<len(read)): 
  subset = []
  for j in range(len(read)):
    if i & (1<<j): 
        print(i, 1<<j)
        subset.append(read[j]) 
  s.append(subset)
for i in range(1,len(s)):
    if sum(s[i]) == b:
        cnt+=1
print(cnt)