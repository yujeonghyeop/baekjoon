a, b, c = input().split()
if int(b) >= int(c):
    print(-1)
else:
    print(int(a)//(int(c)-int(b))+1)
