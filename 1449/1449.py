import sys
a,b = list(map(int, sys.stdin.readline().split()))
n = [0] * 1001
read = list(map(int,sys.stdin.readline().split()))
m = max(read)
num = 0
for i in range(a):
    n[read[i]] = 1
for i in range(m+1):
    if n[i] == 1:
        if i==1000:
            num+=1
        else:
            for j in range(i,i+b):
                if j==1001:
                    break
                n[j] = 0
            num+=1
print(num)