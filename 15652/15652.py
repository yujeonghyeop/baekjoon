import sys
a,b = map(int, sys.stdin.readline().split())
s=[]
def dfs():
    if len(s)==b:
        print(' '.join(map(str,s)))
        return
    for i in range(1,a+1):
        if len(s)==0:
            s.append(i)
            dfs()
            s.pop()
        else:
            if s[-1]<=i:
                s.append(i)
                dfs()
                s.pop()
dfs()