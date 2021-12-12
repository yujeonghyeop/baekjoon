n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    dis = b-a
    cnt = 4
    c = 2
    while(True):
        if c >= dis:
            break
        else:
            c += cnt
            cnt += 2
    if c-(cnt-2)//2< dis <=c:
        print(cnt-2)
    else:
        print(cnt-3)
