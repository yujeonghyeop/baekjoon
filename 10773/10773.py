a = int(input())
answer = []
for i in range(a):
    b = int(input())
    if b!=0:
        answer.append(b)
    else:
        answer.pop()
print(sum(answer))