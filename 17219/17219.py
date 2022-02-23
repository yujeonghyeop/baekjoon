import sys
a,b = list(map(int, sys.stdin.readline().split()))
pw = {}
for i in range(a):
    read = sys.stdin.readline().split()
    pw[str(read[0])] = read[1]
print(pw['noj.am'])

for i in range(b):
    cnt = input()
    print(pw[cnt])