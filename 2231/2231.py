a = int(input())
for i in range(a):
    l = len(str(i))
    cnt = 0
    for j in range(l):
        cnt += int(str(i)[j])
    if cnt+i == a:
        print(i)
        break
    elif i == a-1:
        print(0)
