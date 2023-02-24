s = input()
n = int(input())
answer = 0
ring = []
for i in range(n):
    a = input()
    ring.append(a+a)
for i in range(n):
    if s in ring[i]:
        answer +=1
print(answer)