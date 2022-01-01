import math
import sys
a, b = map(int, sys.stdin.readline().split())
qnswk = 1
qnsah = 1
qnsah = math.factorial(b)
for i in range(b):
    qnswk = qnswk * a
    a -= 1
print(qnswk//qnsah)
