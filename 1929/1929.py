a, b = map(int, input().split())
answer = []
sieve = [True]*(b+1)
m = int(b**0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i+i, b+1, i):
            sieve[j] = False
for j in range(a, b+1):
    if sieve[j] == True:
        answer.append(j)
for k in range(len(answer)):
    print(answer[k])
