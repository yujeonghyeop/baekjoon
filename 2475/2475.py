a, b, c, d, e = input().split()
answer = 0
a = int(a)**2
b = int(b)**2
c = int(c)**2
d = int(d)**2
e = int(e)**2
answer = (a+b+c+d+e) % 10
print(answer)
