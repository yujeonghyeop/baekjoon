a = int(input())
cnt = 0
i = 666
while(True):
    if '666' in str(i):
        cnt += 1
    if cnt == a:
        print(i)
        break
    i += 1
