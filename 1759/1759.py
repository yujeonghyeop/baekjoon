import sys
def dfs(k):
    if len(s)==a:
        mo = 0
        ja = 0
        for i in range(len(s)):
            if s[i]=='a' or s[i]=='u' or s[i]=='i' or s[i]=='e' or s[i]=='o':
                mo+=1
            else:
                ja+=1
        if mo>=1 and ja>=2:
            print(''.join(s))
        return
    if k==b:
        return
    for i in range(k,b):
        if read[i] not in s:
            s.append(read[i])
            k+=1
            dfs(k)
            s.pop()
a,b = list(map(int, sys.stdin.readline().split()))
read = sys.stdin.readline().split()
read = sorted(read)
s = []
dfs(0)