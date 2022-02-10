import sys
n, x, y = list(map(int, sys.stdin.readline().split()))
ans = 0
while(n != 0):
    n -= 1
    if x < 2**n and y < 2**n:  # 1사분면
        ans += 0
    elif x < 2**n and y >= 2**n:  # 2사분면
        ans += (4**n)*1
        y -= (2**n)
    elif x >= 2**n and y < 2**n:  # 3사분먄
        ans += (4**n)*2
        x -= (2**n)
    elif x >= 2**n and y >= 2**n:  # 4사분면
        ans += (4**n)*3
        x -= (2**n)
        y -= (2**n)
print(ans)
