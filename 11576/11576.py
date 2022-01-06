import sys
import string
fbase, nbase = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
read = sys.stdin.readline().split()
tmp = []
answer=[]
for i in range(nbase):
    tmp.append(i)
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        answer.append(tmp[r])
    else:
        answer.append((tmp[r]))
        return convert(q, base)


cnt = 1
ans = 0
for i in reversed(range(n)):
    ans += int(read[i])*cnt
    cnt = cnt*fbase
convert(ans, nbase)
for i in reversed(range(len(answer))):
    if i == 0:
        print(answer[i])
    else:
        print(answer[i], end=' ')
