import sys

a = sys.stdin.readline().split()
cnt = int(a[0],2)
print(oct(cnt)[2:])