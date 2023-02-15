import sys
n = int(input())
fun = []
ans = 0
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    if len(fun) == 0:
        fun.append([a,b])
    else:
        if fun[-1][1] > a:
            if fun[-1][1] <b:
                fun[-1][1] = b
        else:
            fun.append([a,b])
for i in fun:
    c,d = i[0],i[1]
    ans += d-c
print(ans)