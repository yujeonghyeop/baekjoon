import sys
n = int(sys.stdin.readline())
answer = []
realanswer = []
dict = {}
read = sys.stdin.readline().split()
for i in range(n):
    answer.append(int(read[i]))
cnt = sorted(list(set(answer)))
dict = {cnt[j]: j for j in range(len(cnt))}

for k in answer:
    print(dict[k], end=' ')
