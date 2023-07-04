import sys
up = []
right = []
n = int(input())
start = 0
fruit = []
for i in range(6):
    a,l = map(int,sys.stdin.readline().split())
    fruit.append([a,l])
    if i == 0:
        start = a
    if a == 3 or a== 4:
        up.append(l)
    elif a == 1 or a==2 :
        right.append(l)
maxup = max(up)
maxright = max(right)
weight = maxup * maxright
cnt = 2
temp = 1
for j in range(len(fruit)):
    if fruit[j][0] == fruit[(j+2)%6][0]:
        if j == 0 and fruit[1][0] !=fruit[3][0]:
            temp = temp * fruit[j][1]
        else:
            temp = temp * fruit[(j+cnt)%6][1]
            cnt=0
print((weight-temp)*n)