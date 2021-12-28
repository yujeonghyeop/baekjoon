import sys
import collections
n = int(sys.stdin.readline())
a = collections.deque()
d = {}
answer = []
b = -1
max = 0
cnt1 = []
read = sys.stdin.readline().split()
for p in range(len(read)):
    if read[p] not in d.keys():
        d[read[p]] = 1
    else:
        d[read[p]] += 1
for q in range(len(read)):
    a.append([int(read[q]), d[read[q]]])
j = n-2
cnt = a.pop()
while(len(a) != 0):
    if int(d[read[j]]) < cnt[1]:
        answer.append(cnt[0])
        cnt1.append(cnt)
        cnt = a.pop()
        j -= 1
    else:
        if len(cnt1) != 0:
            cnt2 = cnt1.pop()
            if int(d[read[j]]) < cnt2[1]:
                answer.append(cnt2[0])
                cnt1.append(cnt2)
                cnt = a.pop()
                j -= 1
        else:
            answer.append(-1)
            cnt = a.pop()
            j -= 1
for k in reversed(range(len(answer))):
    print(answer[k], end=' ')
print(-1)
