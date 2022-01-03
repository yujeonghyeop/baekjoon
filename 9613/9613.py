import sys
import math
n = int(sys.stdin.readline())
for i in range(n):
    answer = 0
    read = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(read)-1):
        for k in range(j+1, len(read)):
            answer += math.gcd(read[j], read[k])
    print(answer)
