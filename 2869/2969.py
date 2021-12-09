import math
a, b, v = map(int, input().split())
h = math.ceil((v-a)/(a-b))
if a == v:
    print(1)
else:
    print(h+1)
