import sys
from itertools import permutations
n = int(sys.stdin.readline())
city = []
cnt=[]
for i in range(n):
    read = list(map(int, sys.stdin.readline().split()))
    city.append(read)
    cnt.append(i)
s = []
answer = []
for i in permutations(cnt,n):
    ans = 0
    go = True
    for j in range(n-1):
        if city[i[j]][i[j+1]]==0:
            go = False
        ans += city[i[j]][i[j+1]]
    if city[i[-1]][i[0]]==0:
        go = False
    else:
        ans += city[i[-1]][i[0]]
    if go == True:
        answer.append(ans)
print(min(answer))