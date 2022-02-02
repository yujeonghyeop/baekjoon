import sys
def dfs():
    if len(s)==b:
        print(' '.join(map(str,s)))
    for i in range(a):
        if read[i] not in s:
            if len(s)==0:
                s.append(read[i])
                dfs()
                s.pop()
            else:
                if s[-1]<read[i]:
                    s.append(read[i])
                    dfs()
                    s.pop()

a,b = map(int,input().split())
read = list(map(int,sys.stdin.readline().split()))
s=[]
read.sort()
dfs()
