import sys
n = int(sys.stdin.readline())
read = list(map(int, sys.stdin.readline().split()))
for i in range(n-1,0,-1):
    if read[i-1]> read[i]:
        for j in range(n-1,0,-1):
            if read[i-1]>read[j]:
                read[i-1],read[j] = read[j],read[i-1]
                read = read[:i] + sorted(read[i:],reverse=True)
                print(*read)
                exit()
print(-1)
