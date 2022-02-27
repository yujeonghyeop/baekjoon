import sys
n = int(sys.stdin.readline())
read = sys.stdin.readline().split()
arr = [[1] * n for _ in range(n)]
s = []
k=0
def possible(g):
    v=0
    for i in range(g,-1,-1):
        v += s[i]
        if arr[i][g] == '+' and v <=0:
            return False
        if arr[i][g] == '0' and v!=0:
            return False
        if arr[i][g] == '-' and v >=0:
            return False
    return True
def dfs(q):
    if len(s)==n:
        print(' '.join(map(str,s)))
        exit()
    for i in range(-10,11):
        s.append(i)
        if possible(q):
            dfs(q+1)
        s.pop()
for i in range(n):
    for j in range(i,n):
        arr[i][j] = read[0][k]
        k+=1
dfs(0)