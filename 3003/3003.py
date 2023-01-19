import sys
find = list(map(int, sys.stdin.readline().split()))
chess = [1,1,2,2,2,8]
for i in range(len(chess)):
    chess[i] = chess[i] - find[i]
print(*chess)