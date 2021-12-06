def selfnum(n):
    cnt = 0
    n = str(n)
    for i in range(len(n)):
        cnt = cnt + int(n[i])
    cnt += int(n)
    return cnt


answer = [0]*10000000
l = []
for i in range(10000):
    a = selfnum(i)
    answer[a] = 1
for j in range(1, 10000):
    if answer[j] == 0:
        print(j)
