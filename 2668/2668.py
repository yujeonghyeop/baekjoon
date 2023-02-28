n = int(input())
a = []
parent = [0] * (n+1)
answer = []
ranswer = []
a.append(0)
for i in range(1,n+1):
    parent[i] = i

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    number = int(input())
    a.append(number)
for j in range(1,n+1):
    if find(parent,j) == find(parent,a[j]):
        cnt = []
        cnt.append(a[j])
        k=a[j]
        while(True):
            if j == a[k]:
                cnt.append(a[k])
                break
            else:
                cnt.append(a[k])
                k = a[k]
        answer.append(cnt)
    else:
        union(parent,j,a[j])
for i in range(len(answer)):
    for j in range(len(answer[i])):
        ranswer.append(answer[i][j])
ranswer = list(set(ranswer))
ranswer = sorted(ranswer)
print(len(ranswer))
for i in range(len(ranswer)):
    print(ranswer[i])