import sys
m, n = map(int, input().split())
rec = []
for i in range(m):
    rec.append(input())
print(rec[0])
cntl = 0
cntr = 0
cntw = 0
cntb = 0
answer = []
for k in range(8, m+1):
    for i in range(8, n+1):
        for p in range(cntr, k):
            for j in range(cntl, i):
                if (p+j) % 2 == 0:
                    if rec[p][j] != 'W':
                        cntw += 1
                    if rec[p][j] != 'B':
                        cntb += 1
                else:
                    if rec[p][j] != 'W':
                        cntb += 1
                    if rec[p][j] != 'B':
                        cntw += 1
        cntl += 1
        answer.append(cntw)
        answer.append(cntb)
        cntw = 0
        cntb = 0
    cntr += 1
    cntl = 0
print(min(answer))
