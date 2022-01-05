import sys
sieve = [True]*(1000001)
m = int(1000001**0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i*2, 1000001, i):
            sieve[j] = False
a = int(sys.stdin.readline())
for i in range(a):
    count = 0
    b = int(sys.stdin.readline())
    for j in range(2, b//2+1):
        if sieve[j] == True:
            if sieve[b-j] == True:
                count += 1
    print(count)
