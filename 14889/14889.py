import sys
import copy
n = int(sys.stdin.readline())
power = []
s=[]
answer = []
for i in range(n):
    read = list(map(int,sys.stdin.readline().split()))
    power.append(read)
def dfs(k):
    if k==n:
        return
    if len(s)==n//2:
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
        answer.append(diff)
        return
    for i in range(k,n):
        if i not in s:
            s.append(i)
            k+=1
            dfs(k)
            s.pop()
dfs(0)
print(min(answer))
