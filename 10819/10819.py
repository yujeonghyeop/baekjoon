import sys
from itertools import permutations

n = int(sys.stdin.readline())
read = list(map(int, sys.stdin.readline().split()))
answer = []
read = sorted(read)

for i in permutations(read, n):
    cnt = 0
    for j in range(len(i)-1):
        cnt+=abs(i[j] - i[j+1])
    answer.append(cnt)
print(max(answer))