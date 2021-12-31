import math
import sys
a, b = map(int, sys.stdin.readline().split())
qnsah = math.factorial(b)
qnswk = 1
answer = 0
for i in range(b):
    qnswk = qnswk*a
    a -= 1
cnt = str(qnswk//qnsah)
for j in reversed(range(len(cnt))):
    if cnt[j] == '0':
        answer += 1
    else:
        print(answer)
        break
