import sys
n = int(sys.stdin.readline())
answer=[0]*10001
for i in range(n):
    a=int(sys.stdin.readline())
    answer[a]=answer[a]+1
for i in range(10001):
    if answer[i]!=0:
        for j in range(answer[i]):
            print(i)
