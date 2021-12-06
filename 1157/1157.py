a = input()
a = a.upper()
b = {}
for i in range(len(a)):
    if a[i] in b:
        b[a[i]] += 1
    else:
        b[a[i]] = 1
c = list(b.values())
if c.count(max(c)) != 1:
    print('?')
else:
    b = sorted(b.items(), key=lambda x: x[1], reverse=True)
    print(b[0][0])
