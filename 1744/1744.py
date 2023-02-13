n = int(input())
cal = []
for i in range(n):
    a = int(input())
    cal.append(a)
cal = sorted(cal)
cnt = []
ans = 0
countzero = 0
underzero = []
while(len(cal)!= 0):
    a = cal.pop()
    if a > 1:
        cnt.append(a)
    elif a == 0:
        countzero +=1
    elif a == 1:
        ans += 1
    elif a <0:
        underzero.append(a)
    if len(cnt) == 2:
        ans += cnt[0] * cnt[1]
        cnt = []
if len(cnt) != 0:
    ans += cnt[0]
underzero = sorted(underzero, reverse=True)
while(len(underzero) > 1):
    b = underzero.pop()
    c = underzero.pop()
    ans += b*c
if len(underzero) ==1:
    if countzero == 0:
        ans += underzero[0]
print(ans)