while(True):
    n = int(input())
    answer = 0
    if n == 0:
        break
    else:
        b = 2*n
        sieve = [True]*(b+1)
        m = int(b**0.5)
        for i in range(2, m+1):
            if sieve[i] == True:
                for j in range(i*2, b+1, i):
                    sieve[j] = False
        for k in range(n+1, b+1):
            if sieve[k] == True and k != 0 and k != 1:
                answer += 1
    print(answer)
