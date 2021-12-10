num = int(input())
answer = []
for i in range(num):
    a = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    floor = int(input())
    k = int(input())
    for j in range(1, k+1):
        a[0].append(j)
    for p in range(1, floor+1):
        cnt = 0
        for q in range(len(a[0])):
            cnt += a[p-1][q]
            a[p].append(cnt)
    answer.append(a[floor][k-1])
    print(answer[i])
