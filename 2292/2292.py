a = int(input())
count = 1
cnt = 1
for i in range(a):
    if cnt >= a:
        break
    else:
        cnt = cnt+count*6
        count += 1

print(count)
