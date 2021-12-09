a = int(input())
cnt = 1
count = 1
wk = 0
ah = 0
while(True):
    if count > a:
        if cnt % 2 != 0:
            wk = cnt-((cnt-1) - (a-(count-(cnt-1))))
            ah = ((cnt-1) - (a-(count-(cnt-1))))
            break
        else:
            ah = cnt-((cnt-1) - (a-(count-(cnt-1))))
            wk = ((cnt-1) - (a-(count-(cnt-1))))
            break
    count += cnt
    cnt += 1
print("{}/{}".format(wk, ah))
