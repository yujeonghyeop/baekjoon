import sys
ch = sys.stdin.readline().rstrip('\n')
n = int(sys.stdin.readline())
nch = 100
mins = 10000000
if n == 0:
    print(min(len(ch), abs(100-int(ch))))
else:
    br = list(map(int, sys.stdin.readline().split()))
    for i in range(1000000):
        answer =0
        cnt = list(str(i))
        check = True
        for j in range(len(cnt)):
            if int(cnt[j]) in br:
                check = False
                break
        if check == True:
            if abs(i-int(ch)) < mins:
                mins = abs(i-int(ch))
                answer = i
    if answer ==0:
        print(abs(nch-int(ch)))
    else:
        print(min(len(str(answer))+abs(answer-int(ch)), abs(nch-int(ch))))
