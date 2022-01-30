import sys
a,b = map(int, input().split())
read = list(map(int,sys.stdin.readline().split()))
read.sort()
s=[]
def dfs():
    if len(s)==b:
        print(' '.join(map(str,s)))
        return
    for i in read:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()