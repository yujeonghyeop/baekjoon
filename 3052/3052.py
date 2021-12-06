cnt = []
for i in range(10):
    a = int(input())
    cnt.append(a % 42)
print(len(list(set(cnt))))
