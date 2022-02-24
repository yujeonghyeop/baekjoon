import sys
import copy
n = int(sys.stdin.readline())
power = []
s=[]
answer = []
for i in range(n):
    read = list(map(int,sys.stdin.readline().split()))
    power.append(read)
def dfs(p,k):
    if k==n+1:
        return
    if len(s)==p:
        a=[]
        a = [x for x in range(n)]
        cnt = []
        cnt =[x for x in a if x not in s]
        start = 0
        diff = 0
        link = 0
        for i in range(len(s)):
            for j in range(len(s)):
                start +=power[s[i]][s[j]]
        for i in range(len(cnt)):
            for j in range(len(cnt)):
                link += power[cnt[i]][cnt[j]]
        if start>=link:
            diff = copy.deepcopy(start-link)
        else:
            diff = copy.deepcopy(link-start)
        if diff==0:
            answer.append(diff)
            print(0)
            exit()
        answer.append(diff)
        return
    for i in range(k,n):
        if i not in s:
            s.append(i)
            k+=1
            dfs(p,k)
            s.pop()
for i in range(1,n//2+1):
    dfs(i,0)
print(min(answer))
