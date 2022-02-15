import sys
from itertools import combinations, permutations
n = int(sys.stdin.readline())
for i in range(n):
    fashion = {}
    cnt = []
    answer = 1
    a = int(sys.stdin.readline())
    for i in range(a):
        read = sys.stdin.readline().split()
        if read[1] not in fashion:
            fashion[read[1]] = [read[0]]
        else:
            fashion[read[1]] += [read[0]]
    b = sorted(fashion.items(), key=lambda x: x[0])
    for i in range(len(b)):
        cnt.append(len(b[i][1]))
    for i in range(len(cnt)):
        answer = (cnt[i] + 1)*answer
    print(answer-1)