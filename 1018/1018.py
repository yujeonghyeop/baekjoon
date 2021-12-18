import sys
m, n = map(int, input().split())
rec = []
for i in range(m):
    color = sys.stdin.readline().split()
    print("color=", color[0][0])
    rec.append(color)
print(rec)
