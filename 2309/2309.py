cnt = []
for i in range(9):
    cnt.append(int(input()))
cnt.sort()
print(cnt)
for i in range(9):
    for j in range(i+1, 9):
        if sum(cnt) - cnt[i] - cnt[j] == 100:
            cnt[i] = 0
            cnt[j] = 0
            break
for i in range(9):
    if cnt[i] != 0:
        print(cnt[i])
