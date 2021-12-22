import sys
n = int(sys.stdin.readline())
for i in range(n):
    cnt = []
    check = True
    a = sys.stdin.readline()
    for j in range(len(a)-1):
        if a[j] == '(':
            cnt.append(a[j])
        else:
            if len(cnt) == 0:
                print('NO')
                check = False
                break
            else:
                cnt.pop()
    if len(cnt) != 0 and check == True:
        print('NO')
    elif len(cnt) == 0 and check == True:
        print('YES')

