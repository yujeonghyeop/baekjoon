n = int(input())
sieve = [True]*(n+1)
answer = []
cnt = []
p = 0
if n == 1:
    print()
else:
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i*2, n+1, i):
                sieve[j] = False
    for k in range(2, len(sieve)):
        if sieve[k] == True:
            cnt.append(k)
    while(n != 1):
        if n % cnt[p] == 0:
            n = n//cnt[p]
            print(cnt[p])
        else:
            p += 1
