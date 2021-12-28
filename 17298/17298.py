import sys
import collections
n = int(sys.stdin.readline())
a = collections.deque()
answer = []
b = -1
max = 0
cnt1 = []
read = sys.stdin.readline().split()
j = n-2
for i in range(len(read)):
    a.append(int(read[i]))
cnt = a.pop()
while(len(a) != 0):
    if int(read[j]) < cnt:
        answer.append(cnt)
        cnt1.append(cnt)
        cnt = a.pop()
        j -= 1
    else:
        if len(cnt1) != 0:
            cnt2 = cnt1.pop()
            if int(read[j]) < cnt2:
                answer.append(cnt2)
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
