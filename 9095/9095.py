import sys
n = int(sys.stdin.readline())
d = [0]*12
d[1] = 1
d[2] = 2
d[3] = 3
answer = [0]*12
answer[1] = 1
answer[2] = 2
answer[3] = 4
answer[4] = 7
for i in range(5, 12):
    d[i-1] = d[i-2]+d[i-3]+d[i-4]
    answer[i] = answer[i-1] + d[i-1]
for j in range(n):
    a = int(sys.stdin.readline())
    print(answer[a])
