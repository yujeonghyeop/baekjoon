import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
find = int(input())
answer = a.count(find)
print(answer)