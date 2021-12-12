a = int(input())
b = int(input())
answer = []
sieve = [True] * (b+1)
m = int(b ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i+i, b+1, i):
            sieve[j] = False
for k in range(a, b+1):
    if sieve[k] == True:
        if k != 1:
            answer.append(k)
if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))
