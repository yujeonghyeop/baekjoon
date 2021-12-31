import sys
a=100000
sieve = [True]*a
m = int(a**0.5)
for j in range(2, m+1):
    if sieve[j] == True:
        for k in range(j*2, a, j):
            sieve[k] = False
while(True):
    a = int(sys.stdin.readline())
    if a == 0:
        break
    else:
        answer = []
        for k in range(2, a//2+1):
            if sieve[k] == True:
                if sieve[a-k] == True:
                    print("{} = {} + {}".format(a, k, a-k))
                    break
