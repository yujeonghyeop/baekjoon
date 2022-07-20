import sys
a,b,c = map(int,sys.stdin.readline().split())
if a==b and b==c:
    print(1000*a + 10000)
elif a==b:
    print(100*a+1000)
elif b==c:
    print(100*b+1000)
elif a==c:
    print(100*a+1000)
else:
    print(max(a,b,c)*100)