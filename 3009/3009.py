rkfh = []
tpfh = []
answer = []
for i in range(3):
    a, b = map(int, input().split())
    rkfh.append(a)
    tpfh.append(b)
for k in range(len(rkfh)):
    if rkfh.count(rkfh[k]) == 1:
        answer.append(rkfh[k])
        break
for j in range(len(tpfh)):
    if tpfh.count(tpfh[k]) == 1:
        answer.append(tpfh[k])
        break
print(answer)
