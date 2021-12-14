while(True):
    a, b, c = map(int, input().split())
    cnt = []
    cnt.append(a)
    cnt.append(b)
    cnt.append(c)
    cnt = sorted(cnt)
    if cnt[0] == 0:
        break
    else:
        if int(cnt[0]*cnt[0])+int(cnt[1]*cnt[1]) == int(cnt[2]*cnt[2]):
            print("right")
        else:
            print("wrong")
