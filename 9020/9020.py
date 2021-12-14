n = int(input())
for i in range(n):
    a = int(input())
    sieve = []
    answer = []
    minus = []
    cnt = []
    sieve = [True]*a
    m = int(a**0.5)
    for j in range(2, m+1):
        if sieve[j] == True:
            for k in range(j*2, a, j):
                sieve[k] = False
    for p in range(2, a//2+1):
        if sieve[p] == True:
            if sieve[a-p] == True:
                minus.append(abs(p-(a-p)))
                answer.append([p, a-p])
    print(*answer[minus.index(min(minus))])
