import sys
import copy
n = int(sys.stdin.readline())
read = sys.stdin.readline().split()
answer = []
j = 0
def dfs():
    global j
    if len(s) == n+1:
        cnt = copy.deepcopy(s)
        answer.append(cnt)
        return
    for i in range(10):
        if i not in s:
            if read[j] == '<':
                if s[-1] < i:
                    s.append(i)
                    j+=1
                    dfs()
                    s.pop()
                    j-=1
            else:
                if s[-1]>i:
                    s.append(i)
                    j+=1
                    dfs()
                    s.pop()
                    j-=1
for i in range(10):
    s = []
    s.append(i)
    dfs()
print(''.join(map(str,answer[-1])))
print(''.join(map(str,answer[0])))
