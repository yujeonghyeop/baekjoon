a = int(input())
if a % 2 == 0:
    if (a & (a-1)) == 0:
        print(a)
    else:
        print(4*((a-2**(len(bin(a))-3))//2))
else:
    cnt = 4*(((a-1)-2**(len(bin(a-1))-3))//2)
    if a == 1:
        print(1)
    elif cnt+2 > a:
        print(2)
    else:
        print(cnt+2)
