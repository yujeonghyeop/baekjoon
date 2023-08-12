a = input()
tmp = []
sum = 0
for i in a:
    tmp.append(i)
for j in tmp:
    sum += int(j)
if sum % 3 == 0:
    tmp = sorted(tmp, reverse=True)
    print(int(''.join(tmp)))
else:
    print(-1)