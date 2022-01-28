a,b = map(int,input().split())
cnt = [[]for x in range(a**b)]
n = a**(b-1)
for i in range(b):
    for j in cnt:
